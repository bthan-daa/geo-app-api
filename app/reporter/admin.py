from django.contrib import admin
from .models import Incidence, Park


class IncidenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_reported', 'location')
    search_fields = ('title',)
    filter_fields = ('title', 'date_reported')

class ParkAdmin(admin.ModelAdmin):
    list_display = ('ogf_id', 'admin_zone')
    search_fields = ('ofg_id',)
    filter_fields = ('ofg_id',)

admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(Park, ParkAdmin)