"""
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
https://djangostars.com/blog/django-pytest-testing/

A.I. generated code.
Setup: The setUp method initializes the RequestFactory and sets up the URL and test data.
Valid Form Test:
    Creates a POST request with valid data.
    Checks if the response status code is 302 (redirect).
    Verifies that a MovieStatus object with the given tconst exists.
    Confirms the redirect URL is correct.
Invalid Form Test:
    Creates a POST request with invalid data.
    Checks if the response status code is 200 (form re-rendered).
    Verifies that the response contains the error message for the required field.
"""

from django.test import TestCase, RequestFactory
from django.urls import reverse
from django import forms
import re


from movie_reviews.models import MovieStatus
from movie_reviews.forms import AddMovieForm
from movie_reviews.views import AddMovieView


class TestAddMovieView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.good_url = "https://www.imdb.com/title/tt0118799/?ref_=int_ratm_tt_i_2"
        cls.bad_url_no_id = "https://www.imdb.com/title/0118799/?ref_=int_ratm_tt_i_2"
        cls.bad_url_wrong_site = (
            "https://www.ign.com/title/tt0118799/?ref_=int_ratm_tt_i_2"
        )

    def setUp(self):
        self.url = reverse("movie_reviews:movie-add")

    def test_get_form_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movie_reviews/movie_add.html")

    def test_post_valid_data(self):
        # note: valid tconst are added or retrieved from the database
        regex = re.compile("^tt[0-9]+")
        tconst = list(filter(lambda id: regex.match(id), self.good_url.split("/")))[0]
        data = {"imdb_id": self.good_url}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        movie_status = MovieStatus.objects.filter(tconst=tconst)
        self.assertTrue(movie_status.exists())
        self.assertEqual(
            response.url,
            reverse("movie_reviews:movie-detail", kwargs={"pk": movie_status[0].id}),
        )

    def test_post_invalid_data(self):
        # Test for when url is not associated with the IMdB website.
        data = {"imdb_id": self.bad_url_wrong_site}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)  # Ensure it does not redirect
        self.assertContains(
            response, "URL does not originate from IMDb.com."
        )  # Check for form error

        # Test for when url contains no or an invalid tconst (the movie id from imdb tt<numbers>)
        data = {"imdb_id": self.bad_url_no_id}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "URL does not contain the tconst movie id.")


class TestMovieDetailView(TestCase):
    """
    What to test:
    - connection:
        + to this view
        + from this view to review add/update/delete

    """

    @classmethod
    def setUpTestData(cls):
        NotImplemented

    def setUp(self):
        NotImplemented
