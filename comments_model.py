
from datetime import datetime
from extensions import db  # Import the db instance from extensions

# Create Model
class Comment(db.Model):
    __tablename__ = 'comments'  # Specify the table name
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(255))
    faculty_id = db.Column(db.Integer, nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

 

    def __repr__(self):
        return f'<Comment {self.name}>'
