
DATABASE = "weight_lifter_db"


class User:
    optionalAttributes = ['age', 'bio', 'username']
    def __init__(self, data):
        self.id = data['id'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.username = data['username'],
        self.age = data['age'],
        self.email = data['email'],
        self.bio = data['bio'],
        self.password = data['password'],
        self.acc_setup = data['acc_setup']
        

    