from rest_framework import serializers
from messenger.models import Chat
class ChatSerializer(serializers.ModelSerializer):
	class Meta:
		model=Chat
		fields=('__all__')


