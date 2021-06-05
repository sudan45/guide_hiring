from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('register',views.Userviewset)





urlpatterns = [
    path('',include(router.urls)),

    path('login/',views.login , name="login")
]

