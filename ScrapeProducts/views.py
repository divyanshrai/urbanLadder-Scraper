from django.shortcuts import render
from rest_framework import permissions, status, viewsets, generics, status, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from util.choices import VT_URLS, ROOM_TYPE
from rift.settings import MEDIA_ONLINE_ROOT


class ProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []