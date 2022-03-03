from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(PerformanceTime)
admin.site.register(Schedule)
admin.site.register(Date)
admin.site.register(Building)
admin.site.register(City)
admin.site.register(Movie)
admin.site.register(MovieBuilding)