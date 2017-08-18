from mongoengine import Document
from mongoengine.fields import StringField

from graphene_mongoengine import MongoengineObjectType


class Example(Document):
    a_field = StringField()


class Example_Graphene(MongoengineObjectType):
    class Meta:
        model = Example
