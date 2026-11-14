users_db = [
    {
        "id": 1,
        "name": "Garfield",
        "age": 8
    },
    {
        "id": 2,
        "name": "Peter",
        "age": 40
    },
]

class User:
    def __init__(self, _name, _age, _id):
        self.id = _id
        self.name = _name
        self.age = _age

    @classmethod
    def get_user(self, user_id):
        for user_data in users_db:
            if user_data.get("id") == user_id:
                return self(
                    _id=user_data.get("id"),
                    _name=user_data.get("name"),
                    _age=user_data.get("age"),
                )

    @classmethod
    def get_users(self):
        return [
            self(
                _id=user_data.get("id"),
                _name=user_data.get("name"),
                _age=user_data.get("age"),
            )
            for user_data in users_db
        ]
        
    @classmethod
    def delete_user_by_id(self, user_id):
        for index, user_data in enumerate(users_db):
            if user_data.get("id") == user_id:
                del users_db[index]
                return True
        return False
    
    def delete(self):
        if self.id is None:
            return False
        
        self.delete_user_by_id(self.id)
            