from django.urls import path
from .views import Register, loginuser

urlpatterns = [
    # path("postcraft/", home, name='home'),
    path("register/", Register, name='register'),
    path("login/", loginuser, name='login')
]