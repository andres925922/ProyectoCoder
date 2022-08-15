from django.contrib.auth.models import User
from Base.exceptions import BaseEntityNotFoundError

def get_my_user(username = None) -> User:
    if username:
        try:
            return User.objects.get(username = username)
        except:
            raise BaseEntityNotFoundError

    return None
