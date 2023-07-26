from api import ma
from api.models import pet_model
from marshmallow import fields

class PetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = pet_model.PetModel
        load_instance = True
        fields = ('id', 'pet_name', 'pet_type', 'size', 'color', 'breed', 'age', 'user', 'pet_id')

    pet_name = fields.String(required=True)
    pet_type = fields.String(required=True)
    size = fields.String(required=True)
    color = fields.String(required=True)
    breed = fields.String(required=True)
    age = fields.Integer(required=True)
    user = fields.Integer(required=True)
    pet_id = fields.Integer(required=True)



