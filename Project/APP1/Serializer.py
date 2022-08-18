from rest_framework import serializers
from .models import Pipes
class PipesSerializer(serializers.Serializer):
    class Meta:
        model = Pipes
        fields = "__all__"