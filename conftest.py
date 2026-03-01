import pytest
from main import BooksCollector

@pytest.fixture
def collection():
    collextion = BooksCollector()
    return collection

def pytest_make_parametrize_id(val):
    return repr(val)

@pytest.fixture
def collection_five_books(collection):
    collect = collection
    books = ['']