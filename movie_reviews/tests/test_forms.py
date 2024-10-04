from django.test import TestCase
from ..forms import AddMovieForm, MovieReviewForm


class AnimalTestCase(TestCase):
    def setUp(self):
        jp, created = MovieStatus.objects.get_or_create(
            tconst="tt0107290",  # jurassic park
            defaults={
                "status": True,
                "priority": False,
                "netflix": True,
                "prime": True,
            },
        )

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        jp = MovieStatus.objects.get(tconst="tt0107290")

        self.assertEqual(jp.tconst, "tt0107290")
