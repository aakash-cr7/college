from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    """ Custom user model """

    phone_number = models.CharField(max_length=10, blank=True, null=True)
    role = models.CharField(max_length=50, default="Student")
    display_picture = models.ImageField(upload_to = 'users/', blank=True, null=True)
    unique_id = models.CharField(max_length=50)

    class Meta:
        unique_together = ('email',)
        verbose_name = 'User'

    def __str__(self):
        return self.name
