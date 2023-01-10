from django.contrib import admin

from apps.cinema.models import *

admin.site.register(Genre)
admin.site.register(Movie)

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Building)

admin.site.register(MovieBuilding)

admin.site.register(MovieBuildingDate)
admin.site.register(PerformanceTime)
admin.site.register(MovieBuildingDateTimes)