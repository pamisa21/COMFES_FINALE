# server.py
from flask import Flask
from models import Users
from faculty_model import Faculty
from comments_model import Comment
from extensions import db  # Import the db instance from extensions
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/ComFES'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the app
db.init_app(app)

# Import the routes from routes.py
with app.app_context():
    from routes import *
    db.create_all()  # Create tables after importing routes

if __name__ == '__main__':
    app.run(debug=True)


