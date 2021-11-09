from django.contrib import admin

from .models import AdvUser


class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fields = (('username', 'email'), ('first_name', 'last_name'),
              ('send_messages', 'is_active', 'is_activated'),
              ('is_staff', 'is_superuser'),
              ('last_login', 'date_joined'),
              'groups', 'user_permissions',)
    readonly_fields = ('last_login', 'date_joined')

admin.site.register(AdvUser, AdvUserAdmin)
