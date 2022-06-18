import math

import pytest

from main import config
from tests.helpers import create_sample_movie


class TestMovies:
    @pytest.mark.parametrize("pages_argument", [2.5, 2.4, 2, 1.5, 1.4, 1, 0.5, 0.4])
    def test_get_paginated_list_successfully(self, authorized_client, session, pages_argument):
        number_of_movies = int(config.ITEMS_PER_PAGE * pages_argument)
        for i in range(number_of_movies):
            create_sample_movie(title=str(i), uuid=str(i), session=session)
        pages = math.ceil(pages_argument)

        for page in range(1, pages + 1):
            response = authorized_client.get(f"/movies?page={page}")

            assert response.status_code == 200
            if page < pages:
                assert len(response.json["items"]) == config.ITEMS_PER_PAGE
            else:
                assert len(
                    response.json["items"]
                ) == number_of_movies - (config.ITEMS_PER_PAGE * (pages - 1))

    def test_get_paginated_list_with_invalid_page_param(self, authorized_client):
        response = authorized_client.get("/movies?page=0")

        assert response.status_code == 400


class TestMovie:
    MOVIE_URL = "/movies/{}"

    def test_get_movie_successfully(self, authorized_client, session):
        movie = create_sample_movie(title="a", uuid="a", session=session)

        response = authorized_client.get(self.MOVIE_URL.format(movie.id))

        assert response.status_code == 200

    def test_get_non_existing_movie(self, authorized_client):
        response = authorized_client.get(self.MOVIE_URL.format(0))

        assert response.status_code == 404
