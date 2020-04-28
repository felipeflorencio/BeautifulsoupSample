from extensions.database import db
from sqlalchemy_serializer import SerializerMixin

# Define a base model for other database tables to inherit
class MediumModel(db.Model, SerializerMixin):

    db = db
    
    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    title =  db.Column(db.Text, nullable=False)
    post_link = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"Post title: {self.title}" 