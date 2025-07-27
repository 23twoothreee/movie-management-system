from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def update(self, instance, validated_data):
        # If video_file not provided in the update payload, preserve the existing one
        if 'video_file' not in validated_data:
            validated_data['video_file'] = instance.video_file
        return super().update(instance, validated_data)
