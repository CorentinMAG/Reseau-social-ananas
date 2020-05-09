from rest_framework import serializers
from messenger.models import Chat
from messenger.views import get_user_contact, verify_participants, add_all_users
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactSerializer(serializers.StringRelatedField):
    def to_representation(self, value):
        info_user = {'email': value.email, 'first_name': value.first_name, 'last_name': value.last_name,
                     'avatar': value.avatar}
        return info_user

    def to_internal_value(self, value):
        return value


class ChatSerializer(serializers.ModelSerializer):
    participants = ContactSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'participants', 'name', 'status', 'avatar')

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
