from api import ma
from api.models import user_model
from marshmallow import fields


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.UserModel
        load_instance = True
        fields = ('id', 'full_name', 'email', 'password', 'cpf', 'street', 'neighborhood', 'cep', 'phone', 'has_pet')

    full_name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    cpf = fields.String(required=True)
    street = fields.String(required=True)
    neighborhood = fields.String(required=True)
    cep = fields.String(required=True)
    phone = fields.String(required=True)
    has_pet = fields.Boolean(required=True)

