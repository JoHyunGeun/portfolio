from . import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    image_file = db.Column(db.String(20), nullable=False)


    def __repr__(self):
        return f"User('{self.username}', '{self.phone_number}', '{self.image_file}')"