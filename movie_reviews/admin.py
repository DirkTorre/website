from django.contrib import admin
from .models import MovieReview, MovieStatus

"""
tutorial: https://books.agiliq.com/projects/django-admin-cookbook/en/latest/change_text.html
"""

@admin.register(MovieStatus)
class MovieStatusAdmin(admin.ModelAdmin):
    list_display = ('tconst', 'status', 'priority','netflix','prime')
    list_filter = ('status', 'priority','netflix','prime')


# register admin classes
@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = ('tconst', 'watch_date', 'enjoyment', 'quality')
    list_filter = ('watch_date', 'enjoyment', 'quality')
    raw_id_fields = ['tconst']
