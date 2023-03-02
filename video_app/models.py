from django.db import models
from PIL import Image


class Films(models.Model):
    name = models.CharField("Имя", max_length=150)
    url = models.SlugField("url", max_length=100, unique=True)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="posters/")
    video = models.FileField(verbose_name="Видосик", upload_to="video/")
    subtitle = models.FileField(verbose_name="subtitle", upload_to="subtitle/", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "film"
        verbose_name_plural = "films"

    def save(self):
        super().save()
        img = Image.open(self.poster.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.poster.path)


class Serial(models.Model):
    name = models.CharField("Имя", max_length=150)
    url = models.SlugField("url", max_length=100, unique=True)
    poster = models.ImageField("Постер", upload_to="posters/")

    class Meta:
        verbose_name = "serial"
        verbose_name_plural = "serials"

    def __str__(self):
        return self.name


class Season(models.Model):
    number = models.SmallIntegerField("Какой сезон")
    name_serial = models.ForeignKey(Serial, verbose_name="Какой сериал", on_delete=models.SET_NULL, null=True)
    url = models.SlugField("url", max_length=100, unique=True)
    poster = models.ImageField("Постер", upload_to="posters/")

    class Meta:
        verbose_name = "season"
        verbose_name_plural = "seasons"

    def __str__(self):
        return str(self.number) + str(self.name_serial)


class Series(models.Model):
    number = models.SmallIntegerField("Какая серия")
    name = models.CharField("Название серии", max_length=150)
    what_serial = models.ForeignKey(Serial, verbose_name="Какой сериал", on_delete=models.SET_NULL, null=True)
    number_season = models.ForeignKey(Season, verbose_name="Какой сезон", on_delete=models.SET_NULL, null=True)
    url = models.SlugField("url", max_length=100, unique=True)
    poster = models.ImageField("Постер", upload_to="posters/")
    video = models.FileField(verbose_name="Видосик", upload_to="video/")
    subtitle = models.FileField(verbose_name="subtitle", upload_to="subtitle/", blank=True)

    class Meta:
        verbose_name = "seria"
        verbose_name_plural = "series"

    def __str__(self):
        return str(self.number) + f" - {self.name}"


class Test(models.Model):
    name = models.CharField("Название серии", max_length=150)
    what_serial = models.ManyToManyField(Serial, verbose_name="Какой сериал", null=True)
