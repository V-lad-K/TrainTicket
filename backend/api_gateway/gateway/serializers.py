from rest_framework import serializers


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    re_password = serializers.CharField(write_only=True)


class UserAuthorizationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class UserResetPasswordConfirmationSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=10)
    token = serializers.CharField(max_length=450)
    new_password = serializers.CharField(write_only=True)
    re_new_password = serializers.CharField(write_only=True)


class UserAccountActivationSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=10)
    token = serializers.CharField(max_length=450)
