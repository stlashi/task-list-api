from flask import current_app
from app import db



class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String)
    tasks = db.relationship('Task', backref='goal', lazy=True)

    def goal_response(self):
        goal_response = {
                "id": self.goal_id,
                "title": self.title
                }
        return goal_response
