from rest_framework import generics, viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Artist, Album, Track
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Artist.objects.all()
        return queryset

    serializer_class = ArtistSerializer

    def create(self, request):
        artist = Artist.objects.filter(
            name=request.data.get('name'),
            owner=request.user
        )
        if artist:
            msg = 'Artist with that name already exists'
            raise ValidationError(msg)
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        artist = Artist.objects.get(pk=self.kwargs["pk"])
        if not request.user == artist.owner:
            raise PermissionDenied("You do not have permission to delete this artist")
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        artist = Artist.objects.get(pk=self.kwargs["pk"])
        if not request.user == artist.owner:
            raise PermissionDenied(
                "You do not have permission to edit this artist"
            )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicArtists(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Artist.objects.all().filter(is_public=True)
        return queryset

    serializer_class = ArtistSerializer


class PublicArtistDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Artist.objects.all().filter(is_public=True)
        return queryset

    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Album.objects.all()
        return queryset

    serializer_class = AlbumSerializer

    def create(self, request):
        album = Album.objects.filter(
            title=request.data.get('title'),
            artist=request.data.get('artist'),
            owner=request.user
        )
        if album:
            msg = 'Album with that name already exists'
            raise ValidationError(msg)
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        album = Album.objects.get(pk=self.kwargs["pk"])
        if not request.user == album.owner:
            raise PermissionDenied("You do have permission to delete this album")
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        album = Album.objects.get(pk=self.kwargs["pk"])
        if not request.user == album.owner:
            raise PermissionDenied(
                "You do not have permission to edit this album"
            )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicAlbums(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Album.objects.all().filter(is_public=True)
        return queryset

    serializer_class = AlbumSerializer


class PublicAlbumDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Album.objects.all().filter(is_public=True)

    serializer_class = AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Track.objects.all()
        return queryset

    serializer_class = TrackSerializer

    def create(self, request):
        track = Track.objects.filter(
            track_title=request.data.get('track_title'),
            album=request.data.get('album'),
            artist=request.data.get('artist')
        )
        if track:
            msg = 'Track with that name already exists'
            raise ValidationError(msg)
        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        track = Track.objects.get(pk=self.kwargs["pk"])
        if not request.user == track.owner:
            raise PermissionDenied("You do not have permission to delete this track")
        return super().destroy(request, *args, **kwargs)

    def update(self , request, *args, **kwargs):
        track = Track.objects.get(pk=self.kwargs["pk"])
        if not request.user == track.owner:
            raise PermissionDenied(
                "You do not have permission to edit this track"
            )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicTracks(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Track.objects.all().filter(is_public=True)
        return queryset

    serializer_class = TrackSerializer


class PublicTrackDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Track.objects.all().filter(is_public=True)

    serializer_class = TrackSerializer


class ArtistAlbums(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.kwargs.get("artist_pk"):
            artist = Artist.objects.get(pk=self.kwargs["artist_pk"])
            queryset = Album.objects.filter(
                owner=self.request.user,
                artist=artist
            )
        return queryset

    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
