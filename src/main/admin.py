from django.contrib import admin

from .models import Category, Place, City, AdditionalImage, Comment
from users.models import AdvUser


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('place', 'author', 'content', 'created_at',)
    list_filter = ('created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    lsit_filter = ('order', 'title')


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('city', '_categories', 'title', 'description', 
                    'address', 'author', 'created_at')
    fields = (('city', 'categories'), 'author', 'title', 'description',
              'address', 'image', 'is_active')
    inlines = (AdditionalImageInline,)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
