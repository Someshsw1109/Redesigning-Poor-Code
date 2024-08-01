class User:  
    def __init__(self, name, user_id):  
        self.name = name  
        self.user_id = user_id  

    def to_dict(self):  
        return {  
            'name': self.name,  
            'user_id': self.user_id  
        }  

    @staticmethod  
    def from_dict(data):  
        return User(data['name'], data['user_id'])