from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import Textarea

from .models import Account


class AccountAdmin(UserAdmin):
    model = Account
    search_fields = ('email', 'first_name',)
    list_filter = ('email', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'first_name', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
        ('Personal', {'fields': ('about',)}),
    )

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})}
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_active',)
        }),
    )


admin.site.register(Account, AccountAdmin)

