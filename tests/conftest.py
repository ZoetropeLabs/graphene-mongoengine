import pytest
import mongoengine


@pytest.fixture(scope="session", autouse=True)
def connect_mongo():
    mongoengine.connect('mongoenginetest', host='mongomock://localhost')
    yield
