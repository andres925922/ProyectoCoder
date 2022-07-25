from django.db import models

from Base.models import Base
from django.contrib.auth.models import AbstractUser, User

from django.contrib import admin

# Create your models here.





# ----------------------------------------------------------------------
# MENSAJERÍA

class Room(Base):
    topic = models.CharField(max_length=100, null= False)
    users = models.ManyToManyField(User)

class Message(Base):
    title = models.CharField(max_length=100, null=False)
    body = models.TextField(null=False)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    to = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='to')
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='sender')
    read = models.BooleanField(default=False)

# -------------------------------------------------------------------------
# AVATAR

class Avatar(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='avatares', null=True, blank=True)



# -------------------------------------------------------------------
# REGISTRATIONS
# -------------------------------------------------------------------

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Avatar)