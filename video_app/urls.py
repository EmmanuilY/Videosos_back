from django.urls import path

from . import views


urlpatterns = [
    path("movie/", views.FilmsViewList.as_view()),
    path("movie/<int:pk>/", views.FilmDetailViewList.as_view()),
    path("serial/", views.SerialViewList.as_view()),
    path("serial/<str:pk>/", views.SeasonViewList.as_view()),
    path("serial/<int:pk>/<slug:slug_season>/", views.SeriesViewList.as_view()),
    path("serial/<int:pk>/<slug:slug_season>/<str:name_series>/", views.seria),
    path("", views.films_and_serial),


]