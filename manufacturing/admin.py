from django.contrib import admin
from .models import ManufacturerAdmin, Blueprint, WholesaleCar, Manufacturer

admin.site.register(ManufacturerAdmin)
admin.site.register(Blueprint)
admin.site.register(WholesaleCar)
admin.site.register(Manufacturer)