from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("random", views.random, name="random"),
    path("newPage", views.newPage, name="newPage"),
    path("add/<int:update>", views.add, name="add"),
    path("wiki/<str:title>/<int:view>", views.content, name="content"),
]
