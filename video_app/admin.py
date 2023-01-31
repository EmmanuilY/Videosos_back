from django.contrib import admin
from .models import Films, Serial, Season, Series, Test
# Register your models here.


@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    list_display_links = ("name", "url")

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    list_display_links = ("name", "url")

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ("name_serial", "number")
    list_display_links = ("name_serial",)

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ("name", "number_season", "number")
    list_display_links = ("name",)

