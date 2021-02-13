from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'county', 'id_no', 'email', 'password']

    def validate(self, attrs):
        """Validate the email"""
        email = attrs.get('email', '')
        if not email:
            raise serializers.ValidationError("The email address is not valid")

        return attrs

    def create(self, validated_data):
        """Create a user with validated data"""
        return User.objects.create_user(**validated_data)
