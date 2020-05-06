from rest_framework import serializers
from apps.api.models import Artist, Album, Track


class TrackSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Track
        fields = ('id', 'artist', 'album', 'track_num', 'track_title',
                  'track_length', 'created_at', 'updated_at', 'owner',
                  'is_public')


class AlbumSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tracks = TrackSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Album
        fields = ('id', 'artist', 'title', 'tracks', 'label', 'release_date', 'created_at',
                  'updated_at', 'owner', 'is_public')


class ArtistSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tracks = TrackSerializer(many=True, read_only=True, required=False)
    albums = AlbumSerializer(many=True, read_only=True, required=False, source='album_artist')

    class Meta:
        model = Artist
        fields = ('id', 'name', 'genre', 'albums', 'tracks', 'biography', 'created_at',
                  'updated_at', 'owner', 'is_public')
