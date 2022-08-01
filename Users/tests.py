from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from .models import Room, Message

class Room_Test_Case(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create_user(
            "user1", "user1@user1.com", "123456"
        )
        self.user2 = User.objects.create_user(
            "user2", "user2@user2.com", "123456"
        )

        self.room = Room.objects.create()
        

    def test_add_user_to_room(self) -> None:
        self.room.users.add(self.user1, self.user2)
        # Comprobar si el hilo de conversación tiene usuarios cargados
        self.assertEqual(len(self.room.users.all()), 2)

    def test_add_message_to_a_room(self) -> None:
        self.room.users.add(self.user1, self.user2)
        msg1 = Message.objects.create(
            body = "Hola buenas",
            sender = self.user1
        )
        msg2 = Message.objects.create(
            body = "Hola buenas",
            sender = self.user1
        )
        self.room.messages.add(msg1, msg2)
        
        test_room = Room.objects.filter( id = self.room.id)[0]
        test_message = test_room.messages.all()[0]

        print(test_room, test_message.body)

        self.assertEqual(test_message.body, "Hola buenas")

    def test_get_room_from_users(self) -> Room:
        self.room.users.add(self.user1, self.user2)
        rooms = Room.objects.filter(users = self.user1).filter(users = self.user2)
        self.assertEqual(self.room, rooms[0])

    

    

