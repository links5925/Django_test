from django.urls import path
from .views import Login, Register, LogOut, UpdateProfile


urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout', LogOut.as_view(), name='logout'),
    path('register', Register.as_view(), name='register'),
    path('profile/update', UpdateProfile.as_view(), name='profile_update'),
]
