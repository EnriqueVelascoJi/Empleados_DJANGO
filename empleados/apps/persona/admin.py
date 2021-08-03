from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import Person, Habilidades
# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    '''Admin View for Person'''

    list_display = (
        'id',
        'complete_name',
        'job',
        'department',)
    list_filter = ('job', 'department',  'habilidades')
    # inlines = [
    #     Inline,
    # ]
    search_fields = ('first_name', 'last_name')
    ordering = ('-id',)
    filter_horizontal = ('habilidades',)

@admin.register(Habilidades)
class HabilidadesAdmin(admin.ModelAdmin):
    '''Admin View for Habilidades'''

    list_filter = ('habilidad',)
    search_fields = ('habilidad',)
    ordering = ('id',)
