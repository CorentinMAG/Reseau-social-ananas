import json
from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message
from .views import get_last_10_messages, get_user_contact, get_current_chat

User = get_user_model()


class ChatConsumer(WebsocketConsumer):

    def fetch_user_messages(self, data):
        messages = get_last_10_messages(data['id'])
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_user_message(content)

    def new_message(self, data):
        user_contact = get_user_contact(data['from'])
        message = Message.objects.create(
            contact=user_contact,
            content=data['message'],
            is_admin=bool(data['status']))
        current_chat = get_current_chat(data['id'])
        current_chat.messages.add(message)
        current_chat.save()
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message),
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        obj = {
            'id': message.id,
            'author': message.contact.first_name,
            'avatar': message.contact.avatar,
            'content': message.content,
            'status': message.is_admin,
            'timestamp': str(message.timestamp)
        }
        if message.contact.photo:
            obj['photo']=message.contact.photo.url
        return obj

    def fetch_channels(self, data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': 'fetch'
            }
        )

    def update_channels(self, data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': data
            }
        )

    def partial_update(self, data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': data
            }
        )

    commands = {
        'new_message': new_message,
        'fetch_user_messages': fetch_user_messages,
        'fetch_channels': fetch_channels,
        'update': update_channels,
        'partialUpdate': partial_update
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'messenger_%s' % self.room_name

        self.group_name_user = str(self.scope['user']).replace("@", ".")
        async_to_sync(self.channel_layer.group_add)(
            self.group_name_user, self.channel_name)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name_user,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def send_user_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.group_name_user,
            {
                "type": "chat_message",
                "message": message,
            },
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))
