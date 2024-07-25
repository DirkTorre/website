from django.contrib import admin
from .models import WatchedDates, WatchedStatus, Availability
# Register your models here.
admin.site.register(WatchedDates)
admin.site.register(WatchedStatus)
admin.site.register(Availability)