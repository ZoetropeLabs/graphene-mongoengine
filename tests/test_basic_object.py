from mongoengine import Document
from mongoengine.fields import StringField, IntField

import graphene
from graphene_mongoengine import MongoengineObjectType


class Person(Document):
    name = StringField()
    thing = IntField(default=20)


class Example_Graphene(MongoengineObjectType):
    class Meta:
        model = Person
        only_fields = ["name"]


class ExampleQuery(graphene.ObjectType):
    persons = graphene.List(Example_Graphene)

    def resolve_persons(self, args, context, info):
        return list(Person.objects().all())


def test_example_model():

    example_person = Person(name="a person")
    example_person.save()

    schema = graphene.Schema(query=ExampleQuery, types=[Example_Graphene])

    result = schema.execute("""
        query {
            persons {
                name
            }
        }
    """)

    assert result.data["persons"][0]["name"] == example_person.name
