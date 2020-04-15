import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

connection = psycopg2.connect(database="production",user="user",password="pass",host="localhost",port=5432)
cursor = connection.cursor()


query = """ INSERT INTO recruit(first_name,surname,chat_name,github_name,id_number,personal_email_address,chort)
VALUES
('Teboho','Matsabu','TG56','TG0111','3691011011','tm@gmail.com','c20 Java'),
('Thabo','Matsabu','TM26','TG0562','9625631452','Tm@gmail.com','c20 Java'),
('Lerato','Mohapi','Mohapi1','LeraMO2','9685635210','Mohapi@gmail.com','c20 Java'),
('Mosa','Mokapela','Mokapela21','Mokapela','8965845236','Mokapela@gmail.com','c19 Web'),
('Papi','Monareng','Papi21','PapoChoo2','9687596652','Choo@gmail.com','c22 Unix')"""

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
    chat_name = db.Column(db.VARCHAR(50))
    github_name = db.Column(db.VARCHAR(50))
    personal_email_address = db.Column(db.VARCHAR(100))
    chort = db.Column(db.VARCHAR)

cursor.execute(query)
connection.commit()
if __name__ == '__main__':
    manager.run()