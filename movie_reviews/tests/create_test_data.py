from django.test import TestCase
from datetime import date

from movie_reviews.models import MovieStatus, MovieReview

"""
Not used (yet).
"""


def create_test_database():
    jp, created = MovieStatus.objects.create(
        tconst="tt0107290",  # jurassic park
        defaults={
            "status": True,
            "priority": False,
            "netflix": True,
            "prime": True,
        },
    )

    room, created = MovieStatus.objects.create(
        tconst="tt0368226",  # the room
        defaults={
            "status": True,
            "priority": False,
            "netflix": False,
            "prime": False,
        },
    )

    reviews = [
        {
            "tconst": jp,
            "watch_date": date(2000, 10, 19),
            "enjoyment": 4.0,
            "quality": 4.0,
            "notes": "awesome",
        },
        {
            "tconst": jp,
            "watch_date": date(2005, 6, 4),
            "enjoyment": 4.0,
            "quality": 4.0,
            "notes": "still awesome",
        },
        {
            "tconst": room,
            "watch_date": date(2010, 3, 9),
            "enjoyment": 2.0,
            "quality": 0.0,
            "notes": "Mistakes were made",
        },
    ]

    for review_data in reviews:
        MovieReview.objects.update_or_create(**review_data)
