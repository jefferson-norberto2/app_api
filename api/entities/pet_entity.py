class PetEntity:
    def __init__(self, pet_name, pet_type, size, color, breed, age, user, pet_id):
        self.pet_name = pet_name
        self.type = pet_type
        self.size = size
        self.color = color
        self.breed = breed
        self.age = age
        self.user = user
        self.pet_id = pet_id

    @property
    def pet_name(self):
        return self._pet_name

    @pet_name.setter
    def pet_name(self, pet_name):
        self._pet_name = pet_name

    @property
    def pet_type(self):
        return self._pet_type

    @type.setter
    def pet_type(self, pet_type):
        self._pet_type = pet_type

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        self._breed = breed

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def pet_id(self):
        return self._pet_id

    @pet_id.setter
    def pet_id(self, pet_id):
        self._pet_id = pet_id

