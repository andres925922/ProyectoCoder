from django.db import models

from Base.models import Base
from django.contrib.auth.models import AbstractUser, User

from django.contrib import admin

# Create your models here.





# ----------------------------------------------------------------------
# MENSAJERÍA

class Message(Base):
    # title = models.CharField(max_length=100, null=False)
    body = models.TextField(null=False)
    # room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    # to = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='to')
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='sender')
    read = models.BooleanField(default=False)

class RoomManager(models.Manager):
    def find(self, user1, user2):
        queryset = self.filter(users = user1).filter(users = user2)
        if len(queryset) > 0:
            return queryset[0]
        else:
            return None

    def find_or_create(self, user1, user2):
        """
        Esta función nos permite o bien encontrar el hilo si es que existe o crear uno nuevo en caso de que no exista pasando como dato dos usuarios diferentes.
        """
        room = self.find(user1, user2)
        if room is None:
            room = Room.objects.create()
            room.users.add(user1, user2)
        return room


class Room(Base):
    users = models.ManyToManyField(
        User,
        related_name='rooms')
    messages = models.ManyToManyField(
        Message,
        related_name ="messages"
    )

    objects = RoomManager()


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