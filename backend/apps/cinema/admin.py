from django.contrib import admin

from apps.cinema.models import *

admin.site.register(Genre)
admin.site.register(City)
admin.site.register(Building)
admin.site.register(PerformanceTime)

admin.site.register(Movie)
admin.site.register(MovieDate)
admin.site.register(MovieDateBuilding)
admin.site.register(MovieDateBuildingVersionSchedule)
