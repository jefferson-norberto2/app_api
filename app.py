from flask import Flask, request
from scripts.scripts_sql import *
from database import Database
import base64


# Create a Flask application
class AppApi:
    def __init__(self):
        self._app = Flask(__name__)
        self._database = None
    
    def create_tables(self):
        self._database = Database(DATABASE_PATH)
        self._database.execute_query(CREATE_USER_TABLE)
        self._database.execute_query(CREATE_PET_TABLE)
        self._database.close_connection()
    
    def sign_up_user(self):
        # Get user data from the request
        self._database = Database(DATABASE_PATH)
        full_name = request.form.get(USER_NAME)
        cpf = request.form.get(CPF)
        email = request.form.get(EMAIL)
        password = request.form.get(PASSWORD)
        street = request.form.get(STREET)
        neighborhood = request.form.get(NEIGHBORHOOD)
        cep = request.form.get(CEP)
        phone = request.form.get(PHONE)
        has_pet = request.form.get(HAS_PET)
        
        # Insert the user data into the database
        query = f'''
            INSERT INTO {USER_TABLE_NAME} (
                {USER_NAME},
                {CPF},
                {EMAIL},
                {PASSWORD},
                {STREET},
                {NEIGHBORHOOD},
                {CEP},
                {PHONE},
                {HAS_PET}
            ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''

        values = (full_name, cpf, email, password, street, neighborhood, cep, phone, has_pet)

        self._database.execute_query(query, values)
        self._database.close_connection()

        # Return a response to the Flutter application
        return 'User registered successfully!'
    
    #TODO: Add pet to database
    def add_pet(self):
        self._database = Database(DATABASE_PATH)
        # Get pet data from the request
        pet_name = request.form.get('pet_name')
        type = request.form.get('type')
        size = request.form.get('size')
        color = request.form.get('color')
        breed = request.form.get('breed')
        age = request.form.get('age')
        user = request.form.get('user')

        # Insert the pet data into the database
        self._database.execute_query(f'''
                                    INSERT INTO pets (
                                        {pet_name},
                                        {type},
                                        {size}, 
                                        {color}, 
                                        {breed}, 
                                        {age}, 
                                        {user}
                                        )'''
                                     )
        

        # Return a response to the Flutter application
        return 'Pet registered successfully!'
    
    def login(self):
        self._database = Database(DATABASE_PATH)
        # Get user data from the request
        email = request.form.get('email')
        password = request.form.get('password')

        # Search for the user in the database
        user = self._database.fetch_one('''
            SELECT * FROM users
            WHERE email=? AND password=?
        ''', (email, password))

        self._database.close_connection()
        # Return a response to the Flutter application
        if user:
            return {'id': user[0], 'name': user[1], 'email': user[3]}
        else:
            return None
    
    def run(self):
        self._app.add_url_rule('/register', 'register', self.sign_up_user, methods=['POST'])
        self._app.add_url_rule('/login', 'login', self.login, methods=['POST'])
        self._app.add_url_rule('/add_pet', 'add_pet', self.add_pet, methods=['POST'])

        self.create_tables()
        try:
            self._app.run(debug=True)
        except Exception as e:
            print(e)

    @staticmethod
    def save_image_from_base64(image_data, save_path):
        # Decode the base64-encoded image string
        image_bytes = base64.b64decode(image_data)

        # Save the image file
        with open(save_path, "wb") as file:
            file.write(image_bytes)

        return save_path

    def __del__(self):
        if self._database:
            self._database.close_connection()
    
if __name__ == '__main__':
    app = AppApi()
    app.run()
