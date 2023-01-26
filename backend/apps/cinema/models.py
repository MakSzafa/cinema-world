from django.db import models

from datetime import date


class Genre(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Building(models.Model):
    BRAND_CHOICES = [
        ('Cinema city', 'Cinema city'),
        ('Helios', 'Helios'),
        ('Multikino', 'Multikino'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=255, primary_key=True, unique=True)
    city = models.ForeignKey(City, to_field='name', on_delete=models.CASCADE)
    brand = models.CharField(
        max_length=255, choices=BRAND_CHOICES, default='Cinema city')

    class Meta:
        ordering = ('brand', 'city')

    def __str__(self):
        return f'{self.brand}_{self.name}'


class PerformanceTime(models.Model):
    time = models.TimeField(primary_key=True, unique=True)

    class Meta:
        ordering = ('time',)

    def __str__(self):
        return f'{self.time}'


class Movie(models.Model):
    name = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    duration = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='movies/', blank=True, null=True)
    clicked = models.IntegerField(default=0)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/movie-details/{self.id}'


class MovieDate(models.Model):
    movie = models.ForeignKey(
        Movie, related_name='dates', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        ordering = ('movie', 'date')

    def __str__(self):
        return f'{self.movie}_{self.date}'


class MovieDateBuilding(models.Model):
    movie_date = models.ForeignKey(
        MovieDate, related_name='buildings', on_delete=models.CASCADE)
    building = models.ForeignKey(
        Building, to_field='name', on_delete=models.CASCADE)

    class Meta:
        ordering = ('movie_date', 'building')

    def __str__(self):
        return f'{self.movie_date}_{self.building}'


class MovieDateBuildingVersionSchedule(models.Model):
    VERSION_CHOICES = [
        ('2D', '2D'),
        ('3D', '3D'),
    ]
    LANGUAGE_CHOICES = [
        ('ENG', 'ENG (NAPISY PL)'),
        ('PL', 'PL'),
        ('DUB', 'DUBBING PL'),
    ]
    movie_date_building = models.ForeignKey(
        MovieDateBuilding, related_name='versions', on_delete=models.CASCADE)
    version = models.CharField(
        max_length=2, choices=VERSION_CHOICES, default='2D')
    language = models.CharField(
        max_length=20, choices=LANGUAGE_CHOICES, default='ENG')
    schedule = models.ManyToManyField(PerformanceTime)

    class Meta:
        ordering = ('movie_date_building', 'version', 'language')

    def __str__(self):
        return f'{self.movie_date_building}_{self.version}_{self.language}'
