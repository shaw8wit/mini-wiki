from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/<int:view>", views.content, name="content"),
    path("newPage", views.newPage, name="newPage"),
    path("add/<int:update>", views.add, name="add"),
    path("random", views.random, name="random"),
    path("search", views.search, name="search"),
]
