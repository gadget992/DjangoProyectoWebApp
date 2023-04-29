from django.contrib import admin

# Register your models here.

from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    #para que lea solamente
    readonly_fields = ("created", "updated")

admin.site.register(Servicio, ServicioAdmin)

