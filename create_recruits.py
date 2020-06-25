import psycopg2
from flask import Flask

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

connection = psycopg2.connect(database="production",user="user",password="pass",host="localhost",port=5432)
cursor = connection.cursor()


quey = """ INSERT INTO recruit(personal_email_address)
VALUES
('gmatsabu@gmail.com')"""


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@127.0.0.1/production'
db = SQLAlchemy(app)

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    recruit = db.relationship('Recruit',backref='owner',lazy='dynamic')

class Recruit(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    owner_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    first_name = db.Column(db.String(20))
    surname = db.Column(db.String(20))
    chat_name = db.Column(db.String(20))
    github_name = db.Column(db.VARCHAR(50))
    id_number = db.Column(db.VARCHAR(10))
    personal_email_address = db.Column(db.VARCHAR(100))
    chort = db.Column(db.VARCHAR)


 #cursor.execute(query)
 #connection.commit()
if __name__ == '__main__':
    manager.run()    
