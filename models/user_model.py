class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)

class UserModel:
    @staticmethod
    def get_user_by_id(user_id):
        # Example: return dummy user
        return {"id": 1, "username": "admin"}
