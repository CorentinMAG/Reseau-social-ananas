from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions,authentication
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from rest_framework.views import APIView
from messenger.models import Chat, TaggedMessages,Message


from .serializers import ChatSerializer, UserSerializer

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
        queryset = User.objects.all()
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


from rest_framework.decorators import api_view

@api_view(['POST'])
def delete_tag(request):
    user = User.objects.get(email=request.data['user'])
    if user == request.user:
        c = Chat.objects.get(pk=int(request.data['chat']))
        t = c.tag.get(pk=int(request.data['tag_id']))
        t.delete()
        return Response({"message": "ok"})
    else:
        return Response({"message":"Not allowed"})



class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def partial_update(self, request, *args, **kwargs):
        """update le model mais partiellement PATCH"""
        instance = self.get_object()
        update_fields = []

        for user in request.data['participants']:
            u = User.objects.get(email=user)
            instance.participants.add(u)
        for user in request.data['admin']:
            u = User.objects.get(email=user)
            instance.admin.add(u)
        if request.data['name'] != '':
            instance.name = request.data['name']
            update_fields.append('name')
        for tag in request.data['tag']:
            m = instance.messages.get(content=tag)
            try:
                t = TaggedMessages(author=request.user, content=m)
                t.save()
                instance.tag.add(t)
                instance.save()
            except:
                pass

        instance.save(update_fields=update_fields)

        return Response()


class AdminPermission(permissions.BasePermission):
    """
    Global permission check for delete chat.
    """

    def has_object_permission(self, request, view, *args, **kwargs):
        chat = args[0]
        if request.user in chat.admin.all():
            return True
        else:
            return False


class ChatDeleteView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (AdminPermission,)
