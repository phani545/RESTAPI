
from django.urls import path
from .views import *

urlpatterns = [
    path('', Booklist),
    path('add/', post_Book),
   
]
