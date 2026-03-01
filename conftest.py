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
    books = ['Дракула', 'Властелин колец', 'Незнайка на Луне', 'Агата Кристи', '12 стульев']
    genre = ['Ужасы', 'Фантастика', 'Мультфильмы', 'Детективы', 'Комедии']
    for i in range(5):
        collect.add_new_book(books[i])

    for i in range(5):
        collect.set_book_genre(books[i], genre[i])

    return collect