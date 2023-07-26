class UserEntity:
    def __init__(self, full_name, email, password, cpf, street, neighborhood, cep, phone, has_pet):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.cpf = cpf
        self.street = street
        self.neighborhood = neighborhood
        self.cep = cep
        self.phone = phone
        self.has_pet = has_pet



    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def name(self, full_name):
        self._full_name = full_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, street):
        self._street = street

    @property
    def neighborhood(self):
        return self._neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood):
        self._neighborhood = neighborhood

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, cep):
        self._cep = cep

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def has_pet(self):
        return self._has_pet

    @has_pet.setter
    def has_pet(self, has_pet):
        self._has_pet = has_pet

        

