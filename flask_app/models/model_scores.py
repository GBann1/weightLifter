




class Scores:
    def __init__(self,data):
        self.id = data['id'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],
        self.score = data['score'],
        self.note = data['note'],
        self.user_id = data['user_id'],
        self.lifts_id = data['lifts_id']
    