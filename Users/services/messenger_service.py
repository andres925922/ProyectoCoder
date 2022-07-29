from ..models import Message, Room

# Create room
def find_or_create_room(user1, user2):
    room = Room.objects.filter(users = user1).filter(users = user2)

    if room is None:
        room = Room.objects.create()
        room.users.add(user1, user2)
    
    return room
        

# New message

# Read Message

# Update massage