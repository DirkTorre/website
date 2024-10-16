from django.test import TestCase, RequestFactory
from django.urls import reverse, NoReverseMatch
import re
from datetime import date


from movie_reviews.models import MovieStatus, MovieReview
from movie_reviews.views import MovieDetailView


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
    - (done) connection to this view
    - connection to add view
    - connection to update view
    - if the info url is correct
    - if the status form is rendered correctly (form test)
    - if the reviews are redered correctly
    """

    @classmethod
    def setUpTestData(cls):
        # create movie
        cls.movie_strangelove = MovieStatus.objects.create(
            tconst="tt0057012",  # Dr. Strangelove
            status=MovieStatus.STATUS_NOT_WATCHED,
            priority=MovieStatus.PRIORITY_YES,
            netflix=MovieStatus.AVAILABILITY_UNKNOWN,
            prime=MovieStatus.AVAILABILITY_UNKNOWN,
        )

        # create movie with reviews
        cls.movie_brother = MovieStatus.objects.create(
            tconst="tt0190590",  # O Brother, Where Art Thou?
            status=MovieStatus.STATUS_WATCHED,
            priority=MovieStatus.PRIORITY_NO,
            netflix=MovieStatus.AVAILABILITY_UNKNOWN,
            prime=MovieStatus.AVAILABILITY_UNKNOWN,
        )

        # create reviews for the movie
        cls.review1 = MovieReview.objects.create(
            tconst=cls.movie_brother,
            watch_date=date(2002, 12, 31),
            enjoyment=4,
            quality=2,
            notes="Fun fun",
        )

        cls.review2 = MovieReview.objects.create(
            tconst=cls.movie_brother,
            watch_date=date(2010, 8, 20),
            enjoyment=4,
            quality=2,
            notes="Still fun",
        )

    def setUp(self):
        self.movie_detail = "movie_reviews:movie-detail"
        self.movie_review = "movie_reviews:review-add"
        self.movie_review_update = "movie_reviews:review-update"

    def test_post_valid_data(self):
        """Test if an exciting detail view get's loaded correctly."""
        strangelove = {"pk": self.movie_strangelove.id}
        detail_link = reverse(self.movie_detail, kwargs=strangelove)
        response = self.client.post(detail_link)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movie_reviews/movie_details.html")

    def test_post_invalid_data(self):
        """Test if an nonexisting detail view get's loaded correctly."""
        wrong_id = {"pk": -1}
        with self.assertRaises(NoReverseMatch):
            reverse(self.movie_detail, kwargs=wrong_id)

        with self.assertRaises(NoReverseMatch):
            reverse(self.movie_detail)

    # def test_links(self):
    #     """Test if the outgoing links behave like expected."""
    #     strangelove = {"pk": self.movie_strangelove.id}
    #     detail_link = reverse(self.movie_detail, kwargs=strangelove)
    #     response = self.client.post(detail_link)
    #     html_text = response.content.decode("utf-8")

    #     link = f"https://www.imdb.com/title/{self.movie_strangelove.tconst}/"
    #     strangelove_imdb_link = (
    #         f'<a id="imdb_web_link" href="{link}">link to the IMDb movie page</a>'
    #     )
    #     self.assertInHTML(strangelove_imdb_link, html_text)
    #     response = self.client.post(link)
    #     self.assertEqual(response.status_code, 200)

    #     strangelove_add_review_url = reverse(self.movie_review, kwargs=strangelove)
    #     strangelove_add_review_link = f'<a id=add-review href="{strangelove_add_review_url}" class="btn btn-primary">Add Review</a>'
    #     self.assertInHTML(strangelove_add_review_link, html_text)
    #     # TODO: test if link works

    #     # TODO: doe not work, fix this.
    #     strangelove_update_review_url = reverse(
    #         self.movie_review_update, kwargs={"pk": self.review1.id}
    #     )
    #     strangelove_update_review_link = (
    #         f'<a id="review_link" href="{strangelove_update_review_link}">'
    #     )
    #     self.assertInHTML(strangelove_update_review_link, html_text)
