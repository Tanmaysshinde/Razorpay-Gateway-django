from django.contrib import admin
from .models import Forms
class FormdAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount')

admin.site.register(Forms, FormdAdmin)