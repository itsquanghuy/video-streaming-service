from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired

from main import admin, db
from main.models.phone import PhoneModel

from .view import ModelView


class PhoneForm(FlaskForm):
    uuid = StringField("UUID", validators=[DataRequired()])


class PhoneModelView(ModelView):
    def create_form(self, obj=None):
        return PhoneForm()

    def edit_form(self, obj=None):
        return PhoneForm()

    def on_model_change(self, form, model, is_created):
        model.uuid = form.uuid.data


phone_model_view = PhoneModelView(
    PhoneModel,
    db.session,
    name="Phone",
)

admin.add_view(phone_model_view)
