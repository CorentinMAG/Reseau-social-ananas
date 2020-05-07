from rest_framework import serializers
from messenger.models import Chat
from messenger.views import get_user_contact, verify_participants, add_all_users


class ContactSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class ChatSerializer(serializers.ModelSerializer):
    participants = ContactSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'messages', 'participants', 'name', 'status')

    def create(self, validated_data):
        admin = self.context['request'].user
        nom_chat = validated_data['name']
        status = validated_data['status']
        participants = validated_data.pop('participants')
        if participants[0] == 'all':
            users = add_all_users()
            chat = Chat()
            chat.name = nom_chat
            chat.status = status
            chat.save()
            for user in users:
                chat.participants.add(user)
                chat.save()
            return chat
        else:
            try:
                verify_participants(participants)
                chat = Chat()
                chat.name = nom_chat
                chat.status = status
                chat.save()
                for email in participants:
                    contact = get_user_contact(email)
                    chat.participants.add(contact)
                    chat.save()
                return chat
            except:
                return None
