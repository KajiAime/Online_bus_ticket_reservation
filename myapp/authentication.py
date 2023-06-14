# myapp/authentication.py
from django.contrib.auth.backends import ModelBackend
from myapp.models import CustomUser

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, city=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username, city=city)
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None