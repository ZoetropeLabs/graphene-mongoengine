from mongoengine import Document
from mongoengine.fields import StringField

from graphene_mongoengine import MongoengineObjectType


def test_example_model():
    class Example(Document):
        a_field = StringField()

    class Example_Graphene(MongoengineObjectType):
        class Meta:
            model = Example
