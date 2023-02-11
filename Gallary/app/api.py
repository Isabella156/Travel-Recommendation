import json
from app import ma
from .models import Image
from flask_restful import Resource


# schema for data serialization to json
class ImageSchema(ma.Schema):
    class Meta:
        fields = ("id", "link", "site_name", "place_id")
        model = Image


image_schema = ImageSchema()
images_schema = ImageSchema(many=True)


class GetPlaceImages(Resource):
    def get(self, placeid):
        serialized = images_schema.dump(Image.query.filter_by(place_id=placeid).all())
        images_str = json.dumps(serialized)
        return images_str
