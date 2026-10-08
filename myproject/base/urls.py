from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path('cart',cart,name='cart'),
    path('add_cart/<int:id>',add_cart,name='add_cart'),
    path('support',support,name='support'),
    path('know_us',know_us,name='know_us'),
    path("remove/<int:id>",remove,name='remove'),
    path("increment/<int:id>",increment,name='increment'),
    path("decrement/<int:id>",decrement,name='decrement'),
    
]
