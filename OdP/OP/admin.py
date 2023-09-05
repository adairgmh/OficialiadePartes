from django.contrib import admin
from OP.models import Area

# Register your models here.
class AreaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Area, AreaAdmin)