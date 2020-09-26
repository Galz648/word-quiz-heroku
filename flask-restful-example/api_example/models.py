"""Data models."""
from . import db


class UserModel(db.Model):
    """Data model for user accounts."""
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'user'
    
    user_id = db.Column(
        db.Integer, 
        primary_key=True
        )
    
    email = db.Column(
        db.String(20),
        index=True,
        nullable=False, 
        unique=False
        )
    
    words = db.relationship(
        'WordModel', 
        backref='user',
        )
    
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )

    admin = db.Column(
        db.Boolean,
        index=False,
        unique=False,
        nullable=False
    )
    
    def __repr__(self):
        return f"user info: user_id = {self.user_id}, email = {self.email}, words = {self.words}, admin = {self.admin}, created = {self.created})"
 
        @property
        def serialize(self):
            """Return object data in easily serializable format"""
            return {
                'email' : email
            }
 
 
 
class WordModel(db.Model):
    
    """Data model for words"""
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'word' 
    id = db.Column(
        db.Integer, 
        primary_key=True
        )

    word = db.Column(db.String(20),
                     index=True,
                     nullable=False, 
                     unique=True
                     )

    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('user.user_id')
        )

    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )   
    def __repr__(self):
    	return f"word info: user_id - {self.user_id}, word = {self.word}, created = {self.created})"