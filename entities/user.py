class User:
    def __init__(self):
        self.name = None
        self.cpf = None
        self.email = None
        self.password = None
        self.street = None
        self.neighborhood = None
        self.cep = None
        self.phone = None
        self.has_pet = None
    
    def from_json(self, json_data):
        self.name = json_data['name']
        self.cpf = json_data['cpf']
        self.email = json_data['email']
        self.password = json_data['password']
        self.street = json_data['street']
        self.neighborhood = json_data['neighborhood']
        self.cep = json_data['cep']
        self.phone = json_data['phone']
        self.has_pet = json_data['has_pet']
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf,
            'email': self.email,
            'password': self.password,
            'street': self.street,
            'neighborhood': self.neighborhood,
            'cep': self.cep,
            'phone': self.phone,
            'has_pet': self.has_pet
        }

    def from_json_sign_up(self, json_data):
        self.name = json_data['name']
        self.email = json_data['email']
        self.password = json_data['password']
        self.cep = json_data['cep']
        self.has_pet = json_data['havePet']
    
    def from_json_sign_in(self, json_data):
        self.email = json_data['email']
        self.password = json_data['password']
    
    def from_database(self, database_data):
        try:
            self.id = database_data[0]
            self.name = database_data[1]
            self.cpf = database_data[2]
            self.email = database_data[3]
            self.password = database_data[4]
            self.street = database_data[5]
            self.neighborhood = database_data[6]
            self.cep = database_data[7]
            self.phone = database_data[8]
            self.has_pet = database_data[9]
        except Exception as e:
            print('Error from database: ', e)


    def __str__(self):
        return f'{self.name}, {self.cpf}, {self.email}, {self.password}, {self.street}, {self.neighborhood}, {self.cep}, {self.phone}, {self.has_pet}'

    def __repr__(self):
        return f'{self.name}, {self.cpf}, {self.email}, {self.password}, {self.street}, {self.neighborhood}, {self.cep}, {self.phone}, {self.has_pet}'