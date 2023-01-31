from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Series
from .serializers import SeriesDetailSerializer


class SeriesViewSet(viewsets.ViewSet):

    def list(self, request, pk = None, slug_season =None):
        queryset = Series.object.all()
        series = get_object_or_404(queryset, )