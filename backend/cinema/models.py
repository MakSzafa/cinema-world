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

# building - for now it is just cinema 
class Building(models.Model): 
    BRAND_CHOICES = [
        ('Cinema city', 'Cinema city'),
        ('Helios', 'Helios'),
        ('Multikino', 'Multikino'),
        ('Other', 'Other'),
    ]
    category = models.ForeignKey(Category, to_field='name', on_delete=models.CASCADE)
    brand = models.CharField(max_length=255, choices=BRAND_CHOICES, default='Cinema city')
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('brand',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

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
    building = models.ForeignKey(Building, to_field='name', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=2, choices=VERSION_CHOICES, default='2D')
    genre = models.CharField(max_length=255)
    duration = models.CharField(max_length=20)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, default='ENG')
    date = models.DateField(default=date.today)
    schedule = ArrayField(models.CharField(max_length=5))
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='movies/', blank=True, null=True) 
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.building.category.slug}/{self.building.slug}/{self.slug}/'