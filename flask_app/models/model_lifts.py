from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "weight_lifter_db"

class Lifts:
    def __init__(self,data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.name = data['name']
        self.description = data['description']
        self.highscore = data['highscore']


    @classmethod
    def get_lifts_highscore(cls):
        query = "SELECT name, highscore FROM lifts;"
        results = connectToMySQL(DATABASE).query_db(query)
        return results
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM lifts;"
        return connectToMySQL(DATABASE).query_db(query)
    
    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM lifts WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, {'id': id})
        return result
    
    @classmethod
    def write_lift(cls, data):
        query = "INSERT INTO lifts (name, description, highscore) VALUES (%(name)s,%(description)s,%(highscore)s);"
        id = connectToMySQL(DATABASE).query_db(query, data)
        return id
    
    @classmethod
    def edit_lift(cls, data):
        query = "UPDATE lifts SET name = %(name)s, description = %(description)s, highscore = %(highscore)s WHERE id = %(id)s;"
        void = connectToMySQL(DATABASE).query_db(query, data)
        return void