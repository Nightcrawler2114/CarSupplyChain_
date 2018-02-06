from django.contrib import admin
from .models import DealershipAdmin, Dealership, RetailCar, WholesaleDeal

admin.site.register(DealershipAdmin)
admin.site.register(Dealership)
admin.site.register(RetailCar)
admin.site.register(WholesaleDeal)
