from django.contrib import admin
from .models import Department

# Register your models here.s
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    '''Admin View for Department'''

    list_display = (
        'name',
        'short_name',
        'anulate',
    )
    list_filter = ('name',)
    # inlines = [
    #     Inline,
    # ]
    search_fields = ('name',)
    ordering = ('id',)

