from rest_framework import serializers

from .models import Films, Series, Season, Serial


class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = ("name", "url", "description", "poster", "id")


class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        fields = ("name", "url", "poster", "id")


class SeasonSerializer(serializers.ModelSerializer):
    name_serial = serializers.SlugRelatedField(slug_field="url", read_only=True)

    class Meta:
        model = Season
        fields = "__all__"


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = "__all__"


class SeriesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ("name", "url", "poster", "video", "id")


class FilmDetailSerializer(serializers.ModelSerializer):
    """Полный фильм"""

    class Meta:
        model = Films
        fields = ("name", "url", "description", "poster", "video", "id", 'subtitle')
