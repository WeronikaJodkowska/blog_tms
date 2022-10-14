from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    age = serializers.IntegerField(min_value=18, required=False)
