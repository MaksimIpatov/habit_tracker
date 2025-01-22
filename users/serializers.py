from rest_framework import serializers

from users.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "phone_number",
            "city",
            "avatar",
        )


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")

    extra_kwargs = {"password": {"write_only": True}}

    def update(self, instance, validated_data):
        if "password" in validated_data:
            instance.set_password(validated_data["password"])
        return super().update(instance, validated_data)
