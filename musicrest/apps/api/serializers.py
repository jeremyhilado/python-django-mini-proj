from rest_framework import serializers
from apps.api.models import Artist, Album, Track


class ArtistSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Artist
        fields = ('id', 'name', 'genre', 'biography', 'created_at',
                  'updated_at', 'owner', 'is_public')


class AlbumSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Album
        fields = ('id', 'title', 'label', 'release_date', 'created_at',
                  'updated_at', 'owner', 'is_public')


class TrackSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Track
        fields = ('id', 'artist', 'album', 'track_num', 'track_title',
                  'track_length', 'created_at', 'updated_at', 'owner',
                  'is_public')
