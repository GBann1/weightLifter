from flask_app.config.mysqlconnection import connectToMySQL
from flask import session

DATABASE = "weight_lifter_db"


class Scores:
    def __init__(self,data):
        self.id = data['id'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],
        self.score = data['score'],
        self.note = data['note'],
        self.user_id = data['user_id'],
        self.lifts_id = data['lifts_id']
    

    @classmethod
    def get_10_scores(cls):
        #Returns 10 most recent-> Date: Lift: LBS: First Name: Last Name:
        query = "SELECT scores.created_at AS 'Date', lifts.name AS 'Lift:', scores.score AS 'LBS:', users.first_name AS 'First Name:', users.last_name AS 'Last Name:' FROM scores JOIN users ON scores.user_id = users.id JOIN lifts ON scores.lift_id = lifts.id LIMIT 10;"
        results = connectToMySQL(DATABASE).query_db(query)
        #catch empty returns
        if len(results) < 1:
            return []
        return results
    
    @classmethod
    def get_user_10_scores(cls, id):
        query = "SELECT scores.score AS 'LBS', lifts.name AS 'Lift:', scores.note AS 'Note:' FROM scores JOIN lifts ON scores.lift_id = lifts.id LIMIT 10 WHERE scores.user_id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, {'scores.user_id':id})
        #catch empty returns
        if len(results[0]) < 1:
            return []
        return results
    
    @classmethod
    def get_all_scores(cls):
        query = "SELECT scores.created_at AS 'Date', lifts.name AS 'Lift:', scores.score AS 'LBS:', scores.note AS 'Notes:' FROM scores JOIN lifts ON scores.lift_id = lifts.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        #catch empty returns
        if len(results) < 1:
            return []
        return results
    
    @classmethod
    def get_score(cls, id):
        query = "SELECT * FROM scores WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,{'id':id})
        return cls(result[0])
    
    @classmethod
    def write_new_score(cls, data):
        query = "INSERT INTO scores (score, lift_duration, note, user_id, lift_id) VALUES (%(score)s, %(lift_duration)s, %(note)s, %(user_id)s, %(lift_id)s);"
        id = connectToMySQL(DATABASE).query_db(query,data)
        return id
    
    @classmethod
    def edit_score(cls, id):
        query = "UPDATE scores SET lift_duration = %(lift_duration)s, note = %(note)s, lift_id = %(lift_id)s WHERE id = %(id)s;"
        void = connectToMySQL(DATABASE).query_db(query, {'id':id})
        return void
    
    @classmethod
    def delete_score(cls, id):
        query = "DELETE FROM scores WHERE id = %(id)s;"
        void = connectToMySQL(DATABASE).query_db(query,{'id':id})
        return void