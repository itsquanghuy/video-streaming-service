from tests.helpers import create_sample_movie

MOVIE_URL = "/playbacks/{}/current-time"


def test_get_playback_current_time_successfully(authorized_client, session):
    movie = create_sample_movie(title="a", uuid="a", session=session)

    response = authorized_client.get(MOVIE_URL.format(movie.id))

    assert response.status_code == 200


def test_get_playback_current_time_with_non_existent_movie(authorized_client, session):
    response = authorized_client.get(MOVIE_URL.format(1))

    assert response.status_code == 404


def test_update_playback_current_time_successfully(authorized_client, session):
    movie = create_sample_movie(title="a", uuid="a", session=session)

    response = authorized_client.put(MOVIE_URL.format(movie.id), json={"current_time": 1})

    assert response.status_code == 200


def test_update_negative_playback_current_time(authorized_client, session):
    movie = create_sample_movie(title="a", uuid="a", session=session)

    response = authorized_client.put(MOVIE_URL.format(movie.id), json={"current_time": -1})

    assert response.status_code == 400
