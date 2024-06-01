from django.urls import path, include
from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    MovieViewSet
)
from rest_framework import routers

router = routers.DefaultRouter()

router.register("movies", MovieViewSet, basename="movies")

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema-halls/", CinemaHallList.as_view(), name="cinemahall-list"),
    path(
        "cinema-halls/<int:pk>/",
        CinemaHallDetail.as_view(),
        name="cinemahall-detail"
    ),
    path("", include(router.urls))
]

app_name = "cinema"
