from django.contrib import admin
from .models import WatchedDates, WatchedStatus, Availability

"""
tutorial: https://books.agiliq.com/projects/django-admin-cookbook/en/latest/change_text.html
"""

# # Register the admin class with the associated model
# admin.site.register(WatchedDates, WatchedDatesAdmin)
# admin.site.register(WatchedStatus, WatchedStatusAdmin)
# admin.site.register(Availability, AvailabilityAdmin)



@admin.register(WatchedStatus)
class WatchedStatusAdmin(admin.ModelAdmin):
    list_display = ('tconst', 'status', 'priority')
    list_filter = ("status", "priority")


# register admin classes
@admin.register(WatchedDates)
class WatchedDatesAdmin(admin.ModelAdmin):
    list_display = ('tconst', 'watch_date', 'enjoyment')
    list_filter = ('watch_date', 'enjoyment')
    raw_id_fields = ['tconst']



@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('tconst', 'netflix', 'prime')
    list_filter = ('netflix', 'prime')
    raw_id_fields = ['tconst']

