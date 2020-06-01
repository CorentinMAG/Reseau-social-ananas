from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

User = get_user_model()


class Message(models.Model):
    contact = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.contact.email


class Chat(models.Model):
    name = models.CharField(max_length=100, blank=True)
    participants = models.ManyToManyField(User, related_name="chats", blank=True)
    messages = models.ManyToManyField(Message, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=7, blank=True)
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


@receiver(pre_delete, sender=User)
def remove_user_from_chats(sender, instance, **kwargs):
    connected_chats = Chat.objects.filter(participants=instance)
    for chat in connected_chats:
        chat.participants.remove(instance)
        chat.save()
    return
