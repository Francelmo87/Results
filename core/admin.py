from django.contrib import admin
from .models import Result


# Register your models here.


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    search_fields = ['id', 'user', 'protocol', 'name', 'number']
    list_display = ['id', 'user', 'protocol', 'name', 'number', 'result_1', 'result_2', 'active']
