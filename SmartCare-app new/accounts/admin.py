from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'name', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff')

admin.site.register(User, UserAdmin)
