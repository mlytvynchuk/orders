from django.shortcuts import render
from rest_framework.routers import DefaultRouter
# Create your views here.
from .views import *

router = DefaultRouter()
router.register(r'^', CustomerViewSet, basename='user_data')
router.register(r'/<str:pk>/', CustomerViewSet, basename='user_data')

urlpatterns = router.urls 