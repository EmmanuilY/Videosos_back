# Generated by Django 4.1.5 on 2023-01-30 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('url', models.SlugField(max_length=100, unique=True, verbose_name='url')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='posters/', verbose_name='Постер')),
                ('video', models.FileField(upload_to='video/', verbose_name='Видосик')),
                ('subtitle', models.FileField(blank=True, upload_to='subtitle/', verbose_name='subtitle')),
            ],
            options={
                'verbose_name': 'film',
                'verbose_name_plural': 'films',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(verbose_name='Какой сезон')),
                ('url', models.SlugField(max_length=100, unique=True, verbose_name='url')),
                ('poster', models.ImageField(upload_to='posters/', verbose_name='Постер')),
            ],
            options={
                'verbose_name': 'season',
                'verbose_name_plural': 'seasons',
            },
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('url', models.SlugField(max_length=100, unique=True, verbose_name='url')),
                ('poster', models.ImageField(upload_to='posters/', verbose_name='Постер')),
            ],
            options={
                'verbose_name': 'serial',
                'verbose_name_plural': 'serials',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название серии')),
                ('what_serial', models.ManyToManyField(null=True, to='video_app.serial', verbose_name='Какой сериал')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(verbose_name='Какая серия')),
                ('name', models.CharField(max_length=150, verbose_name='Название серии')),
                ('url', models.SlugField(max_length=100, unique=True, verbose_name='url')),
                ('poster', models.ImageField(upload_to='posters/', verbose_name='Постер')),
                ('video', models.FileField(upload_to='video/', verbose_name='Видосик')),
                ('subtitle', models.FileField(blank=True, upload_to='subtitle/', verbose_name='subtitle')),
                ('number_season', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='video_app.season', verbose_name='Какой сезон')),
                ('what_serial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='video_app.serial', verbose_name='Какой сериал')),
            ],
            options={
                'verbose_name': 'seria',
                'verbose_name_plural': 'series',
            },
        ),
        migrations.AddField(
            model_name='season',
            name='name_serial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='video_app.serial', verbose_name='Какой сериал'),
        ),
    ]
