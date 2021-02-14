from django.contrib import admin
from .models import water_tank,lights,water_tank_date,lights_date
# Register your models here.
admin.site.register(water_tank)
admin.site.register(lights)
admin.site.register(water_tank_date)
admin.site.register(lights_date)