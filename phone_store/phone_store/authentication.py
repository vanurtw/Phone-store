from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class EmailBackend(BaseBackend):
    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User:
            return None

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            return User.objects.get(email=username)
        except:
            return None
