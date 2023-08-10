class Pet:
    def __init__(self):
        self.id = None
        self.pet_name = None
        self.type = None
        self.size = None
        self.color = None
        self.breed = None
        self.age = None
        self.user_id = None
        self.lost = None
        self.photo = None

    def from_json(self, json_data):
        self.pet_name = json_data['pet_name']
        self.type = json_data['type']
        self.size = json_data['size']
        self.color = json_data['color']
        self.breed = json_data['breed']
        self.age = json_data['age']
        self.user_id = json_data['user_id']
        self.lost = json_data['lost']
        self.photo = json_data['photo']

    def to_json(self):
        return {
            'pet_name': self.pet_name,
            'type': self.type,
            'size': self.size,
            'color': self.color,
            'breed': self.breed,
            'age': self.age,
            'user_id': self.user_id,
            'lost': self.lost,
            'photo': self.photo
        }