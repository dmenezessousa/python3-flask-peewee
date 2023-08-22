from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict , dict_to_model

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
Pet(name='Luna',animal_type='dog',owner_id=1).save()
Pet(name='Thor',animal_type='dog',owner_id=2).save()

app = Flask(__name__)

#Person endpoint
@app.route('/person', methods=['GET','POST'])
@app.route('/person/<id>', methods=['GET','PUT','DELETE'])
def person_endpoint(id=None):
  if request.method == 'GET':    
    if id:
      return jsonify(model_to_dict(Person.get(Person.id == id)))
    else:
      people_list = []
      for person in Person.select():
        people_list.append(model_to_dict(person))
      return jsonify(people_list)

  if request.method == 'PUT':
    body = request.get_json()
    Person.update(body).where(Person.id == id).execute()
    return 'Person ' + str(id) + ' has been updated.'

  if request.method == 'POST':
    new_person = dict_to_model(Person, request.get_json())
    new_person.save()
    return jsonify({"success": True})
  
  if request.method == 'DELETE':
    Person.delete().where(Person.id == id).execute()
    return "Person " + str(id) + " deleted."
#Pet endpoint
@app.route('/pet',methods=['GET','POST'])
@app.route('/pet/<id>', methods=['GET','PUT','DELETE'])
def pet_endpoint(id=None):
  if request.method == 'GET':
    if id:
      return jsonify(model_to_dict(Pet.get(Pet.id == id)))
    else:
      pet_list = []
      for pet in Pet.select():
        pet_list.append(model_to_dict(pet))
      return jsonify(pet_list)

  if request.method == 'PUT':
    body = request.get_json()
    Pet.update(body).where(Pet.id == id).execute()
    return 'Pet ' + str(id) + ' has been updated.'

  if request.method == 'POST':
    new_pet = dict_to_model(Pet, request.get_json())
    new_pet.save()
    return jsonify({"success": True})

  if request.method == 'DELETE':
    Pet.delete().where(Pet.id == id).execute()
    return "Pet " + str(id) + " deleted."

app.run(debug = True, port = 3000)