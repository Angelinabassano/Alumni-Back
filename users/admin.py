from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'role', 'email', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'role')
    list_filter = ('role', 'is_active')
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': (
        'first_name', 'last_name', 'role', 'profile_picture', 'description', 'phone', 'website', 'linkedin', 'github',
        'school', 'company_name', 'nif')}),
        ('RP asignado', {'fields': ('rp',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'password', 'first_name', 'last_name', 'role', 'profile_picture', 'description', 'phone',
            'website', 'linkedin', 'github', 'school', 'company_name', 'nif', 'rp', 'is_active')
        }),
    )


admin.site.register(User, CustomUserAdmin)
