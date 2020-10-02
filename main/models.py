from main import db

class Image(db.Model):

    image_file = db.Column(db.String(20),primary_key=True, nullable=False , default='default.jpg')

    def __repr__(self):
        return f"Image('{self.image_file})"
