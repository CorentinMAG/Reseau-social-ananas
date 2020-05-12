from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from messenger.models import Chat
from .serializers import ChatSerializer,UserSerializer

User = get_user_model()


def get_user_contact(email):
    user = get_object_or_404(User, email=email)
    return user


class ChatListView(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Chat.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            contact = get_user_contact(email)
            queryset = contact.chats.all()
        return queryset

class AllUser(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset=User.objects.all()
        return queryset


class ChatPublic(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Chat.objects.filter(status='Public')
        return queryset


class ChatDetailView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny,)


class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ChatDeleteView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)
