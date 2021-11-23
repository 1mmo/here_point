from django.contrib import admin

from .models import Category, Place, City, AdditionalImage
from users.models import AdvUser


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    lsit_filter = ('order', 'title')


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('city', 'category', 'title', 'description', 
                    'address', 'author', 'created_at')
    fields = (('city', 'category'), 'title', 'description',
              'address', 'image', 'is_active')
    inlines = (AdditionalImageInline,)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
