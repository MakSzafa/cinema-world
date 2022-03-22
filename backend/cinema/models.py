from django.db import models
from django.contrib.postgres.fields import ArrayField

from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Movie(models.Model):
    VERSION_CHOICES = [
        ('2D', '2D'),
        ('3D', '3D'),
    ]
    LANGUAGE_CHOICES = [
        ('ENG', 'ENG (NAPISY PL)'),
        ('PL', 'PL'),
        ('DUB', 'DUBBING PL'),
    ]

    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    duration = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='movies/', blank=True, null=True) 
    clicked = models.IntegerField()
    version = models.CharField(max_length=2, choices=VERSION_CHOICES, default='2D')
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, default='ENG')
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name}_{self.version}_{self.language}'

    def get_absolute_url(self):
        return f'/{self.slug}/'

class City(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

# building - for now it is just cinema 
class Building(models.Model): 
    BRAND_CHOICES = [
        ('Cinema city', 'Cinema city'),
        ('Helios', 'Helios'),
        ('Multikino', 'Multikino'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, to_field='name', on_delete=models.CASCADE)
    city = models.ForeignKey(City, to_field='name', on_delete=models.CASCADE)
    brand = models.CharField(max_length=255, choices=BRAND_CHOICES, default='Cinema city')

    class Meta:
        ordering = ('brand',)

    def __str__(self):
        return f'{self.city}_{self.name}'

class MovieBuilding(models.Model):
    movie = models.ForeignKey(Movie, related_name='buildings', on_delete=models.CASCADE)
    building = models.ForeignKey(Building, to_field='name', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('building',)

    def __str__(self):
        return f'{self.building}_{self.movie}'

class Date(models.Model):
    date = models.DateField(default=date.today)
    movie_building = models.ForeignKey(MovieBuilding, related_name='dates', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date}_{self.movie_building}'

class Schedule(models.Model):
    name = models.ForeignKey(Date, related_name='performance_times', on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return f'{self.time}_{self.name}'