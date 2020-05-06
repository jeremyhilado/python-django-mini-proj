from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from apps.api.views import (
    ArtistViewSet, PublicArtists,
    PublicArtistDetail, AlbumViewSet, PublicAlbums,
    PublicAlbumDetail, TrackViewSet, PublicTracks,
    PublicTrackDetail, ArtistAlbums
)

router = DefaultRouter()
router.register('artists', ArtistViewSet, basename='artists')
router.register('albums', AlbumViewSet, basename='albums')
router.register('tracks', TrackViewSet, basename='tracks')

custom_urlpatterns = [
    url(r'artists/(P<artist_pk>\d+)/recipes/$', ArtistAlbums.as_view(), name='artist_albums'),
    url(r'public-artists/$', PublicArtists.as_view(), name='public_artists'),
    url(r'public-artists/(?P<pk>\d+)/$', PublicArtistDetail.as_view(), name='public_artist_detail'),
    url(r'public-albums/$', PublicAlbums.as_view(), name='public_albums'),
    url(r'public-album/(?P<pk>\d+)/$', PublicAlbumDetail.as_view(), name='public_album_detail'),
    url(r'public-tracks/$', PublicTracks.as_view(), name='public_tracks'),
    url(r'public-tracks/(?P<pk>\d+)/$', PublicTrackDetail.as_view(), name='public_track_detail'),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
