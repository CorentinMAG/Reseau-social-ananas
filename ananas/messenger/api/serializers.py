from rest_framework import serializers
from messenger.models import Chat, TaggedMessages
from messenger.views import get_user_contact, verify_participants, add_all_users
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff', 'groups', 'user_permissions']


class TagSerializer(serializers.StringRelatedField):
    def to_representation(self,value):
        return {
            'content':value.content.content,
            'timestamp':value.timestamp,
            'author':value.author.email,
            'tag_id':value.pk
        }
    def to_internal_vlue(self,value):
        return value


class ContactSerializer(serializers.StringRelatedField):
    def to_representation(self, value):
        info_user = {'email': value.email, 'first_name': value.first_name, 'last_name': value.last_name,
                     'avatar': value.avatar}
        if value.photo:
            info_user['photo'] = value.photo.url
        return info_user

    def to_internal_value(self, value):
        return value


class ChatSerializer(serializers.ModelSerializer):
    participants = ContactSerializer(many=True)
    tag = TagSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'participants', 'name', 'status', 'admin','tag')

    def create(self, validated_data):
        admin = self.context['request'].user
        nom_chat = validated_data['name']
        status = validated_data['status']
        participants = validated_data.pop('participants')
        chat = Chat()
        chat.name = nom_chat
        chat.status = status
        if participants[0] == 'all':
            users = add_all_users()
            chat.save()
            chat.admin.add(admin)
            for user in users:
                chat.participants.add(user)
                chat.save()
            return chat
        else:
            try:
                verify_participants(participants)
                chat.save()
                chat.admin.add(admin)
                for email in participants:
                    contact = get_user_contact(email)
                    chat.participants.add(contact)
                    chat.save()
                return chat
            except:
                return None
