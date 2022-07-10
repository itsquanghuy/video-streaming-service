from main import db


class MovieModel(db.Model):
    __tablename__ = "movie"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    uuid = db.Column(db.String(36), unique=True, nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    is_a_series = db.Column(db.Boolean, nullable=False)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<MovieModel {self.id}>"


class EpisodeModel(db.Model):
    __tablename__ = "episode"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    season = db.Column(db.Integer, nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    uuid = db.Column(db.String(36), unique=True, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))

    movie = db.relationship("MovieModel", backref="episodes")

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<MovieSeriesModel {self.id}>"
