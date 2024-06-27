from rest_framework import serializers


class UserAuthorization(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
