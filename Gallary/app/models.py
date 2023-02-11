from app import db


# image table for storing the link of images of each places
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(100))
    site_name = db.Column(db.String(50))
    place_id = db.Column(db.Integer)
