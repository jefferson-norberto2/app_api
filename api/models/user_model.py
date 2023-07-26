from api import db
from passlib.hash import pbkdf2_sha256


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    neighborhood = db.Column(db.String(100), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    has_pet = db.Column(db.Boolean, nullable=False)

    def password_encrypt(self, password):
        self.password = pbkdf2_sha256.hash(password)

    def password_decrypt(self, password):
        return pbkdf2_sha256.verify(password, self.password)
    

