from db import db

class TimeCardModel(db.Model):
    __tablename__ = 'timecards'

    id = db.Column(db.Integer, primary_key=True)
    enter = db.Column(db.String(20))
    out = db.Column(db.String(20))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, enter, out, user_id):
        self.enter = enter
        self.out = out
        self.user_id = user_id

    def json(self):
        return {'enter': self.enter, 'out': self.out, 'user_id': self.user_id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_enter(cls, enter):
        return cls.query.filter_by(enter=enter).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()