from main import db


class PhoneModel(db.Model):
    __tablename__ = "phone"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False)

    def __str__(self):
        return self.uuid

    def __repr__(self):
        return f"<UserModel {self.id}>"
