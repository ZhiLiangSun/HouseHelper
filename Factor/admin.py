from django.contrib import admin
from .models import Hospital, Accident, Stolen, Library, Market

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Accident)
admin.site.register(Stolen)
admin.site.register(Library)
admin.site.register(Market)
