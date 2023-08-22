from flask import Flask
from peewee import *
from playhouse import model_to_dict , dict_to_model

db = PostgresqlDatabase('flask_lab', user='peewee', password='',host='localhost',port=5432)

class BaseModel(Model):
  class Meta:
    database = db

#Person schema
class Person(BaseModel):
  name = CharField()
  age = CharField()

class Pet(BaseModel):
  name = CharField()
  animal_type = CharField()
  owner_id = IntegerField()

