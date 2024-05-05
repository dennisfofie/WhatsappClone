
from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4
from enum import Enum

class MessageStatus(Enum):
    read='read'
    unread='unread'
    delivered='delivered'
    typing='typing'

class UserStatus(Enum):
    online='online'
    offline='offline'


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    username = models.CharField(
        null=True, blank=True, max_length=100
    )
    fullName = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(max_length=50, choices=[(status.name, status.value) for status in UserStatus], default='offline')
    active = models.BooleanField(default=False)
    profilePic = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=100, blank=False, null=False)
    modifiedBy = models.CharField(max_length=100, blank=False, null=False)

    REQUIRED_FIELDS= ['password', 'fullName']

    USERNAME_FIELD = 'email'
    

    def __str__(self):
        return self.email


class Tag(models.Model):
    tagId = models.UUIDField(default=uuid4)
    tagged = models.SlugField(max_length=255, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    modifiedBy = models.CharField(max_length=100, null=False, blank=True)




class Message(models.Model):
    chatId = models.BigAutoField(primary_key=True, null=False, blank=False)
    toUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')
    fromUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    chats = models.TextField(max_length=1024, null=True, blank=True)
    taggedUser = models.ForeignKey(Tag, on_delete=models.CASCADE)
    audio = models.FileField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[(status.name , status.value) for status in MessageStatus] )
    createdBy = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    modifiedBy = models.CharField(max_length=100, null=False, blank=True)

    def __self__(self):
        return self.fromUser
    

class Room(models.Model):
    roomId = models.BigAutoField(primary_key=True, null=False, blank=False)
    roomName = models.CharField(max_length=100, null=False, blank=False)
    users = models.ManyToManyField(to=User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    modifiedBy = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.roomName
    

class Thread(models.Model):
    threadId = models.BigAutoField(primary_key=True, null=False, blank=False)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='replied')
    comment = models.TextField(max_length=1024, null=True)
    fileComment = models.FileField(null=False, blank=False)
    imageComment = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    modifiedBy = models.CharField(max_length=100, null=False, blank=True)


class Stat(models.Model):
    statusId = models.BigAutoField(primary_key=True, null=False, blank=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    video = models.FileField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    modifiedBy = models.CharField(max_length=100, null=False, blank=True)

class ResetPassword(models.Model):
    resetUser = models.ForeignKey(User, on_delete=models.CASCADE)
    oldPassword = models.CharField(max_length=150, null=False, blank=False)
    newPassword = models.CharField(max_length=150, blank=False, null=False)
    confirmPassword = models.CharField(max_length=150, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    modifiedBy = models.CharField(max_length=100, null=False, blank=True)
