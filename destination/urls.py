from . import views
from django.urls import path,include
from destination.views import Destinations






urlpatterns = [
   
    path('', Destinations.as_view()),
]

