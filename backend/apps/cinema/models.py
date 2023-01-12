from django.db import models

from datetime import date

class Genre(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

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
    genres = models.ManyToManyField(Genre)
    duration = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='movies/', blank=True, null=True) 
    clicked = models.IntegerField(default=0)
    version = models.CharField(max_length=2, choices=VERSION_CHOICES, default='2D')
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, default='ENG')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}_{self.version}_{self.language}'

    def get_absolute_url(self):
        return f'/movie-details/{self.id}'

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

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

class MovieBuildingDate(models.Model):
    movie_building = models.ForeignKey(MovieBuilding, related_name='dates', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        ordering = ('movie_building',)

    def __str__(self):
        return f'{self.movie_building}_{self.date}'

class PerformanceTime(models.Model):
    time = models.TimeField(primary_key=True, unique=True)

    class Meta:
        ordering = ('time',)

    def __str__(self):
        return f'{self.time}'

class MovieBuildingDateTimes(models.Model):
    name = models.ForeignKey(MovieBuildingDate, related_name='schedule', on_delete=models.CASCADE)
    performance_times = models.ManyToManyField(PerformanceTime)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'