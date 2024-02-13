from rest_framework import serializers
from .models import Like, FeedCard

class FeedCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedCard
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'