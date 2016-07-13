from django.contrib import admin

# Register your models here.
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter =  ['created']

admin.site.register(Image, ImageAdmin)