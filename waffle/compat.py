import django

__all__ = ['User', 'AUTH_USER_MODEL']

# Django 1.5+ compatibility
if django.VERSION >= (1, 5):
    from django.contrib.auth import get_user_model
    from django.conf import settings
    User = get_user_model()
    AUTH_USER_MODEL = settings.AUTH_USER_MODEL
else:
    from django.contrib.auth.models import User
    AUTH_USER_MODEL = 'auth.User'
