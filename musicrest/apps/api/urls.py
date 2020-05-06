from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from apps.api.views import (
    ArtistViewSet, PublicArtists,
    PublicArtistDetail
)

router = DefaultRouter()
router.register('artists', ArtistViewSet, basename='artists')

custom_urlpatterns = [
    url(r'public-artists/$', PublicArtists.as_view(), name='public_artists'),
    url(r'public-artists/(?P<pk>\d+)/$', PublicArtistDetail.as_view(), name='public_artists_detail'),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
