from flask.testing import FlaskClient

from main.models.phone import PhoneModel
from main.models.movie import MovieModel

sample_phone_uuid = "518361D5-B7DA-42D6-9CA6-025CB35BEF80"


class CustomClient(FlaskClient):
    def __init__(self, *args, **kwargs):
        self._headers = {
            'Authorization': f'Bearer {kwargs.pop("token")}',
        }

        super().__init__(*args, **kwargs)

    def _prepare_kwargs(self, kwargs):
        if 'headers' in kwargs:
            kwargs['headers'].update(self._headers)
        else:
            kwargs['headers'] = self._headers

        return kwargs

    def get(self, *args, **kwargs):
        kwargs = self._prepare_kwargs(kwargs)

        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        kwargs = self._prepare_kwargs(kwargs)

        return super().post(*args, **kwargs)

    def put(self, *args, **kwargs):
        kwargs = self._prepare_kwargs(kwargs)

        return super().put(*args, **kwargs)

    def delete(self, *args, **kwargs):
        kwargs = self._prepare_kwargs(kwargs)

        return super().delete(*args, **kwargs)


def create_sample_phone(session) -> PhoneModel:
    phone = PhoneModel(uuid=sample_phone_uuid)
    session.add(phone)
    session.commit()
    return phone


def create_sample_movie(title:str, uuid: str, session) -> MovieModel:
    movie = MovieModel(title=title, description="a", uuid=uuid)
    session.add(movie)
    session.commit()
    return movie
