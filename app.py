from flask import Flask
from peewee import *
# from playhouse import model_to_dict , dict_to_model

db = PostgresqlDatabase('flask_lab', user='peewee', password='',host='localhost',port=5432)

class BaseModel(Model):
  class Meta:
    database = db

#Person schema
class Person(BaseModel):
  name = CharField()
  age = IntegerField()

#Pet schema
class Pet(BaseModel):
  name = CharField()
  animal_type = CharField()
  owner_id = IntegerField()

#Connection and Creating new Tables in database
db.connect()
db.drop_tables([Person, Pet])
db.create_tables([Person,Pet])

#Creating new Person
Person(name='Diego',age=30).save()
Person(name='Thaciana',age=31).save()

#Creating new Pet
Pet(name='Luna',animal_type='dog',owner_id=1)
Pet(name='Thor',animal_type='dog',owner_id=2)

app = Flask(__name__)

#Person endpoint
@app.route('/person', method=['GET','POST'])
@app.route('/person/<id>', method=['GET','PUT','DELETE'])
#Pet endpoint
@app.route('/pet',method=['GET','POST'])
@app.route('/pet/<id>', method=['GET','PUT','DELETE'])

