from flask import Flask, request
from entities.pet import Pet
from scripts.scripts_sql import *
from database import Database
from entities.user import User
from pathlib import Path

# Create a Flask application
class AppApi:
    def __init__(self):
        self._app = Flask(__name__)
        self._database = None
        self.create_tables()
        self.define_routes()

    # Define the routes for the Flask application
    def define_routes(self):
        self._app.add_url_rule('/sign_up', 'sign_up', self.sign_up_user, methods=['POST'])
        self._app.add_url_rule('/sign_in', 'sign_in', self.sign_in, methods=['POST'])
        self._app.add_url_rule('/add_pet', 'add_pet', self.add_pet, methods=['POST'])
        self._app.add_url_rule('/is_online', 'is_online', self.is_online, methods=['GET'])
        self._app.add_url_rule('/lost_pets', 'lost_pets', self.get_lost_pets, methods=['GET'])
        self._app.add_url_rule('/add_lost_pet', 'add_lost_pet', self.add_lost_pet, methods=['GET'])
    
    def create_tables(self):
        self._database = Database(DATABASE_PATH)
        self._database.execute_query(CREATE_USER_TABLE)
        self._database.execute_query(CREATE_PET_TABLE)
        self._database.close_connection()

    def is_online(self):
        return {'Connection': 'Do it!'}
    
    def add_lost_pet(self):
        try:
            pet = Pet()
            pet.pet_name = 'Toto'
            pet.type = 'Gato'
            pet.size = 'Medio'
            pet.color = 'Cinza'
            pet.breed = 'Vira-lata'
            pet.age = 3
            pet.lost = 1
            pet.photo = 'https://www.zooplus.pt/magazine/wp-content/uploads/2020/12/g_2.jpg'

            self._database = Database(DATABASE_PATH)
            # Insert the pet data into the database
            query = f'''
                                        INSERT INTO {PET_TABLE_NAME} (
                                            {PET_NAME},
                                            {TYPE},
                                            {SIZE},
                                            {COLOR},
                                            {BREED},
                                            {AGE},
                                            {LOST},
                                            {PHOTO}
                                            ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)
                                            '''
            values = (pet.pet_name, pet.type, pet.size, pet.color, pet.breed, pet.age, pet.lost, pet.photo)
            self._database.execute_query(query, values)
            self._database.close_connection()
            return {'add_lost_pet': True}
        except Exception as e:
            print(e)
            return {'add_lost_pet': False}

    def get_lost_pets(self):
        self._database = Database(DATABASE_PATH)
        lost_pets = self._database.fetch_data(f'''
            SELECT * 
            FROM {PET_TABLE_NAME}
            WHERE {LOST} = 1
        ''')
        self._database.close_connection()
        return {'lost_pets':lost_pets}
    
    def sign_up_user(self):
        try:
            user = User()
            user.from_json_sign_up(request.form)
            # Get user data from the request
            self._database = Database(DATABASE_PATH)
            
            query = f'''
                SELECT * 
                FROM {USER_TABLE_NAME}
                WHERE {EMAIL} = ?
            '''
            values = (user.email,)
            existent_user = self._database.fetch_one(query, values)

            if existent_user:
                self._database.close_connection()
                return {'sign_up': False}
            
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

            values = (user.name, user.cpf, user.email, user.password, user.street, user.neighborhood, user.cep, user.phone, user.has_pet)

            self._database.execute_query(query, values)
            self._database.close_connection()

            # Return a response to the Flutter application
            return {'sign_up': True}
        except Exception as e:
            return {'sign_up': False}
    
    def add_pet(self):
        try:
            pet = Pet()
            pet.from_json(request.data)

            self._database = Database(DATABASE_PATH)
            # Get pet data from the request

            # Insert the pet data into the database
            self._database.execute_query(f'''
                                        INSERT INTO pets (
                                            {pet.pet_name},
                                            {pet.type},
                                            {pet.size}, 
                                            {pet.color}, 
                                            {pet.breed}, 
                                            {pet.age}, 
                                            {pet.user_id}
                                            )'''
                                        )
            self._database.close_connection()

            # Return a response to the Flutter application
            return {'add_pet': True}
        except Exception as e:
            print(e)
            return {'add_pet': False}
    
    def sign_in(self):
        user = User()
        user.from_json_sign_in(request.form)

        self._database = Database(DATABASE_PATH)

        # Search for the user in the database
        user_from_database = self._database.fetch_one('''
            SELECT * FROM users
            WHERE email=? AND password=?
        ''', (user.email, user.password))

        self._database.close_connection()
        # Return a response to the Flutter application
        if user_from_database:
            user.from_database(user_from_database)
            return {'sign_in': user.to_json()}
        else:
            return {'sign_in': 'Not found'}
    
    def run(self):
        try:
            self._app.run(host='localhost', port=5000, debug=True)
        except Exception as e:
            print(e)


        def __del__(self):
            if self._database:
                self._database.close_connection()
    
if __name__ == '__main__':
    app = AppApi()
    app.run()
