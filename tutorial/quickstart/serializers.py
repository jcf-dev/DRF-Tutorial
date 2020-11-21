from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers

from .models import UserExtension


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UserExtensionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserExtension
        fields = ['url', 'user', 'group', 'department']