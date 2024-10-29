from django.contrib import admin
from .models import MovieReview, MovieStatus, MovieDataFiles

"""
tutorial: https://books.agiliq.com/projects/django-admin-cookbook/en/latest/change_text.html
"""

# register admin classes


@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = ("tconst", "watch_date", "enjoyment", "quality")
    list_filter = ("watch_date", "enjoyment", "quality")
    raw_id_fields = ["tconst"]


@admin.register(MovieStatus)
class MovieStatusAdmin(admin.ModelAdmin):
    list_display = ("tconst", "status", "priority", "netflix", "prime")
    list_filter = ("status", "priority", "netflix", "prime")


@admin.register(MovieDataFiles)
class MovieDataFilesAdmin(admin.ModelAdmin):
    list_display = (
        "file_name",
        "imdb_path",
        "output_path",
        "last_successful_download",
        "progress",
    )
