from django.core.management.base import BaseCommand
from datetime import date

from movie_reviews.models import MovieReview, MovieStatus


class Command(BaseCommand):
    help = "load movie review data"

    def handle(self, *args, **kwargs):

        jp, created = MovieStatus.objects.get_or_create(
            tconst="tt0107290",  # jurassic park
            defaults={
                "status": True,
                "priority": False,
                "netflix": True,
                "prime": True,
            },
        )

        room, created = MovieStatus.objects.get_or_create(
            tconst="tt0368226",  # the room
            defaults={
                "status": True,
                "priority": False,
                "netflix": False,
                "prime": False,
            },
        )

        matrix, created = MovieStatus.objects.get_or_create(
            tconst="tt0133093",  # the Matrix
            defaults={
                "status": True,
                "priority": False,
                "netflix": True,
                "prime": True,
            },
        )

        conan, created = MovieStatus.objects.get_or_create(
            tconst="tt0082198",  # Conan the Barbarian
            defaults={
                "status": False,
                "priority": True,
                "netflix": False,
                "prime": True,
            },
        )

        taxi, created = MovieStatus.objects.get_or_create(
            tconst="tt0075314",  # Taxi Driver
            defaults={
                "status": True,
                "priority": False,
                "netflix": True,
                "prime": True,
            },
        )

        chl, created = MovieStatus.objects.get_or_create(
            tconst="tt0061512",  # Cool Hand Luke
            defaults={
                "status": False,
                "priority": True,
                "netflix": False,
                "prime": False,
            },
        )

        fllasvegas, created = MovieStatus.objects.get_or_create(
            tconst="tt0120669",  # Fear and Loathing in Las Vegas
            defaults={
                "status": True,
                "priority": True,
                "netflix": True,
                "prime": True,
            },
        )

        babyd, created = MovieStatus.objects.get_or_create(
            tconst="tt3890160",  # Baby Driver
            defaults={
                "status": True,
                "priority": True,
                "netflix": False,
                "prime": True,
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
                "tconst": jp,
                "watch_date": date(2015, 2, 5),
                "enjoyment": 4.0,
                "quality": 4.0,
                "notes": "still the best",
            },
            {
                "tconst": room,
                "watch_date": date(2010, 3, 9),
                "enjoyment": 2.0,
                "quality": 0.0,
                "notes": "Mistakes were made",
            },
            {
                "tconst": matrix,
                "watch_date": date(2006, 1, 1),
                "enjoyment": 3.5,
                "quality": 3.5,
                "notes": "amazeballs",
            },
            {
                "tconst": matrix,
                "watch_date": date(2019, 11, 4),
                "enjoyment": 4.0,
                "quality": 3.0,
                "notes": "Still cool",
            },
            {
                "tconst": taxi,
                "watch_date": date(2022, 9, 23),
                "enjoyment": 4.0,
                "quality": 4.0,
            },
            {
                "tconst": fllasvegas,
                "watch_date": date(2017, 1, 20),
                "enjoyment": 4.0,
                "quality": 4.0,
            },
            {
                "tconst": fllasvegas,
                "watch_date": date(2020, 8, 14),
                "enjoyment": 4.0,
                "quality": 4.0,
                "notes": "awesome",
            },
            {
                "tconst": babyd,
                "watch_date": date(2018, 3, 11),
                "enjoyment": 3.0,
                "quality": 3.0,
                "notes": "fun",
            },
        ]

        for review_data in reviews:
            MovieReview.objects.update_or_create(**review_data)
