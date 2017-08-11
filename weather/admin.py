from django.contrib import admin

# Register your models here.
from .models import Rainfall, Station

admin.site.register(Rainfall)
admin.site.register(Station)

