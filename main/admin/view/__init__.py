from flask import Response, redirect
from flask_admin.contrib import sqla
from werkzeug.exceptions import HTTPException

from main import basic_auth


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(
            message,
            Response(
                message, 401, {"WWW-Authenticate": 'Basic realm="Login Required"'}
            ),
        )


class ModelView(sqla.ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException("Not authenticated. Refresh the page.")
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())
