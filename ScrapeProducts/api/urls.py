from ScrapeProducts.views import *
from django.urls import include,path
from rest_framework import routers

router = routers.DefaultRouter()

router.register('product', viewset= ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]