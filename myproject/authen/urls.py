from django.urls import path
from .views import *

urlpatterns = [
    path('',login_,name="login_"),
    path('regiter/',register,name='register'),
    path('profile/',profile,name='profile'),
    path('logout_/',logout_,name="logout_"),
    path('forgot/',forgot,name='forgot'),
    path('update/',update,name='update'),
    path('reset/',reset,name='reset'),
    path('new_password/',new_password,name='new_password')

]
