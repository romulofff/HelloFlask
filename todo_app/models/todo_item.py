from todo_app.db import db

class Todo_item(db.Model):
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))

    def __init__(self, content):
        self.content = content 