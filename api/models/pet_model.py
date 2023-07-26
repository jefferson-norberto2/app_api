from api import db

class PetModel(db.Model):
    __tablename__ = 'pets'
    pet_id = db.Column(db.Integer, primary_key=True, nullable=False)
    pet_name = db.Column(db.String(50), nullable=False)
    pet_type = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    breed = db.Column(db.String(50), nullable=False)
    age = db.Column(db.String(50), nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))

