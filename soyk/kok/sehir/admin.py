from django.contrib import admin
from .models import City
@admin.register(City)
class SehirAdmin(admin.ModelAdmin):
    list_display = ('Ilce', 'Mahalle')