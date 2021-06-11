from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('register',views.Userviewset)





urlpatterns = [
    path('',include(router.urls)),

    path('login/',views.login , name="login"),
    path('guide_profile/<int:pk>/', views.Guide_profile.as_view()),
    path('tourist_profile/<int:pk>/', views.Tourist_profile.as_view()),
    path('destination/', views.Destinations.as_view()),
]

