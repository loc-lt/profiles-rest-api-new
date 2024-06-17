from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes the name for testing our APIView"""
    name = serializers.CharField(max_length=10)