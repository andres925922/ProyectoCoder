from django.test import TestCase
from Base.services.base_service import get_avatar

# Create your tests here.


def get_avatar_test(user):
    return get_avatar(user)
