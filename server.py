from flask import Flask
from models import db, Users  # Import db and Users model
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/our_users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the app
db.init_app(app)

# Import the routes from routes.py
from routes import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables in the database
    app.run(debug=True)
