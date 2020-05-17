from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
import hashlib

User = get_user_model()


class Message(models.Model):
    contact = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.contact.email


class Chat(models.Model):
    name = models.CharField(max_length=100,blank=True)
    participants = models.ManyToManyField(User, related_name="chats",blank=True)
    messages = models.ManyToManyField(Message, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=7,blank=True)
    avatar = models.URLField(max_length=200, blank=True)
    admin = models.ManyToManyField(User, related_name='admin', blank=True)

    def __str__(self):
        return "{}".format(self.pk)


@receiver(post_save, sender=User)
def Connect_user_to_public_chat(sender, instance, **kwargs):
    try:
        PublicChat = Chat.objects.filter(status='Public')
        for chat in PublicChat:
            chat.participants.add(instance)
    except:
        return


@receiver(post_save, sender=Chat)
def Random_avatar_chat(sender, instance, **kwargs):
    md5_nom = hashlib.md5()
    md5_nom.update(instance.name.encode('utf8'))
    avatar = "https://www.gravatar.com/avatar/{}?d=retro".format(md5_nom.hexdigest())
    sender.objects.filter(pk=instance.pk).update(avatar=avatar)
