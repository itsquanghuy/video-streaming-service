from main import db


class PlaybackModel(db.Model):
    __tablename__ = "playback"

    phone_id = db.Column(db.Integer, db.ForeignKey("phone.id"), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), primary_key=True)
    current_time = db.Column(db.Integer, nullable=False, default=0)

    phone = db.relationship("PhoneModel", uselist=False, backref="playbacks")
    movie = db.relationship("MovieModel", uselist=False)

    def __repr__(self):
        return f"<PlaybackModel {self.id}>"
