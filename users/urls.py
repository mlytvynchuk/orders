from django.shortcuts import render
from rest_framework.routers import DefaultRouter
# Create your views here.
from .views import *

router = DefaultRouter()
router.register('', CustomerViewSet, basename='user_data')

urlpatterns = router.urls 