from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import StreamingHttpResponse
from .models import Films, Serial, Season, Series
from .services import open_file
from .serializers import FilmsSerializer, FilmDetailSerializer, SerialSerializer, SeasonSerializer, SeriesSerializer, \
    SeriesDetailSerializer


# Create your views here.

class FilmsViewList(generics.ListCreateAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer
    permission_classes = [permissions.AllowAny]


class SerialViewList(generics.ListCreateAPIView):
    queryset = Serial.objects.all()
    serializer_class = SerialSerializer
    permission_classes = [permissions.AllowAny]


class SeasonViewList(generics.ListCreateAPIView):
    serializer_class = SeasonSerializer
    print()

    def get_queryset(self):
        return Season.objects.filter(name_serial=self.kwargs["pk"])

    permission_classes = [permissions.AllowAny]


class SeriesViewList(generics.ListCreateAPIView):
    serializer_class = SeriesSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Series.objects.filter(what_serial=self.kwargs["pk"]).filter(number_season=self.kwargs["slug_season"])


class SeriesDetailView(generics.ListCreateAPIView):
    serializer_class = SeriesDetailSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Series.objects.filter(url=self.kwargs["name_series"])


class FilmDetailViewList(generics.RetrieveAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response


@api_view(['GET'])
def films_and_serial(request):
    if request.method == 'GET':
        serials = Serial.objects.all()
        films = Films.objects.all()

        projects_serializer = SerialSerializer(serials, many=True, context={'request': request})
        news_serializer = FilmsSerializer(films, many=True, context={'request': request})
        data = projects_serializer.data + news_serializer.data
        return Response(data)


@api_view(['GET'])
def seria(request, **kwargs):
    if request.method == 'GET':
        seria = Series.objects.get(url=kwargs["name_series"])
        seria_serilizer = SeriesDetailSerializer(seria, many=False, context={'request': request})
        data = seria_serilizer.data
        return Response(data)


class SeriesTestView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Series.objects.all()
    serializer_class = SeriesDetailSerializer
