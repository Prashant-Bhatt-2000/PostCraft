from django.urls import path
from .views import AllPosts, Write_article, YourPosts, logout_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", AllPosts, name='post'),
    path("write/", Write_article, name="writearticle"),
    path("stories/", YourPosts, name="yourPosts"),
    path('logout/', logout_view, name='logout'),
]