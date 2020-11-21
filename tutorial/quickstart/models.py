from django.db import models
from django.contrib.auth.models import User, Group

class UserExtension(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ManyToManyField(Group)
    department = models.CharField(max_length=150)
