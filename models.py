"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

PROFILE_IMAGE = "https://i.pinimg.com/736x/04/8b/8d/048b8dbc061a104f266176b1b7bf828c.jpg"

class User(db.Model):
    "each user on the blog"
    __tablename__ = "users"
   
    #call in all table - 'blogly' elements
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=PROFILE_IMAGE)
    
    # combines first_name and last_name together
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
   
    # connects to database in flask app
    def connect_db(app):

    db.app = app
    db.init_app(app)
    
    
    
    