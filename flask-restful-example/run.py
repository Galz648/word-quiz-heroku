from flask import Flask, jsonify

from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)



app = Flask(__name__)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    words = db.relationship('Word', backref='user')
    
    def __repr__(self):
    	return f"user info: user- {id}, name = {name}, words = {words})"
 
class word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
    	return f"user info: user_id - {user_id}, word = {word})"




@app.route('/')
def index():
    return 'Hello world'

# Example : /api/word/define?word='{word}'
@app.route('/api/word/define')
def define():
        return jsonify({'data':'word definition'})

       
# Example : /api/word/related?word='{word}'
@app.route('/api/word/related')
def related():

        return jsonify({'data':'related words'})

    
# Example : /api/word/sentences?word='{word}'
@app.route('/api/word/sentences')
def sentences():
        return jsonify({'data':'example sentences'})


if __name__ == "__main__":
    #app.run(debug=True)
    db.create_all()
