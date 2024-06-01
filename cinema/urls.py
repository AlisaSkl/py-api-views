from django.urls import path, include
from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)
from rest_framework import routers

router = routers.DefaultRouter()

router.register("movies", MovieViewSet, basename="movies")

cinema_halls_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})
cinema_halls_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema-halls/", cinema_halls_list, name="cinemahall-list"),
    path(
        "cinema-halls/<int:pk>/",
        cinema_halls_detail,
        name="cinemahall-detail"
    ),
    path("", include(router.urls))
]

app_name = "cinema"
