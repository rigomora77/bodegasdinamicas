from django.contrib import admin
from .models import Store, Part, Inventory

admin.site.register(Store)
admin.site.register(Part)
admin.site.register(Inventory)
