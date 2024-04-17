from django.contrib import admin
from .models import Room

# Register your models here.

class roomAdmin(admin.ModelAdmin):
    list_display=['id','address']

admin.site.register(Room,roomAdmin)
