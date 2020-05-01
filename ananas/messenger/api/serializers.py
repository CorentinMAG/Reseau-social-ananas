from rest_framework import serializers
from messenger.models import Chat
from messenger.views import get_user_contact


class ContactSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class ChatSerializer(serializers.ModelSerializer):
    participants = ContactSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'messages', 'participants')

    def create(self, validated_data):
        participants = validated_data.pop('participants')
        chat = Chat()
        chat.save()
        for email in participants:
            contact = get_user_contact(email)
            chat.participants.add(contact)
        chat.save()
        return chat
