DATABASE_PATH = 'petfriendly.db'

USER_TABLE_NAME = 'users'
PET_TABLE_NAME = 'pets'

USER_NAME = 'user_name'
CPF = 'cpf'
EMAIL = 'email'
PASSWORD = 'password'
STREET = 'street'
NEIGHBORHOOD = 'neighborhood'
CEP = 'CEP'
PHONE = 'phone'
HAS_PET = 'has_pet'


PET_NAME = 'pet_name'
TYPE = 'type'
SIZE = 'size'
COLOR = 'color'
BREED = 'breed'
AGE = 'age'
USER = 'user'
LOST = 'lost'
PHOTO = 'photo'


CREATE_USER_TABLE = f'''
    CREATE TABLE IF NOT EXISTS {USER_TABLE_NAME} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        {USER_NAME} TEXT NOT NULL,
        {CPF} TEXT,
        {EMAIL} TEXT NOT NULL UNIQUE ON CONFLICT FAIL,
        {PASSWORD} TEXT NOT NULL,
        {STREET} TEXT,
        {NEIGHBORHOOD} TEXT,
        {CEP} TEXT NOT NULL,
        {PHONE} TEXT,
        {HAS_PET} INTEGER
    )
'''

CREATE_PET_TABLE = f'''
    CREATE TABLE IF NOT EXISTS {PET_TABLE_NAME} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        {PET_NAME} TEXT NOT NULL,
        {TYPE} TEXT NOT NULL,
        {SIZE} TEXT NOT NULL,
        {COLOR} TEXT NOT NULL,
        {BREED} TEXT NOT NULL,
        {AGE} INTEGER NOT NULL,
        {USER} INTEGER,
        {LOST} INTEGER NOT NULL,
        {PHOTO} TEXT,
        FOREIGN KEY ({USER}) REFERENCES {USER_TABLE_NAME}(id)
    )
        '''