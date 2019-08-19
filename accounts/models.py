from django.db import models
from django.conf import settings
# Create your models here.
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# Model to store the list of logged in users
class LoggedInUser(models.Model):
    user = models.OneToOneField(User, related_name='logged_in_user', on_delete=models.CASCADE)
    # Session keys are 32 characters long
    session_key = models.CharField(max_length=32, null=True, blank=True)
    login_time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user.username
