import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_enable_default_genre_success(self, collection):
        first_book = 'Властелин колец'
        collection.add_new_book(first_book)
        assert collection.get_book_genre(first_book) == ''

    @pytest.mark.parametrize('book', ['', 'Властелин колец Властелин колец Властелин колец'])
    def test_add_new_book_with_incorrect_name_not_added(self, book, collection):
        collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 0

    def test_add_new_book_add_repeated_books_not_added(self, collection):
        books = ['Властелин колец', 'Властелин колец']
        for book in books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 1

    def test_set_book_genre_added(self, collection):
        first_book = 'Властелин колец'
        genre = 'Фантастика'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, genre)
        assert collection.get_book_genre(first_book) == genre

    def test_set_book_genre_change(self, collection):
        first_book = 'Властелин колец'
        genre = 'Фантастика'
        new_genre = 'Ужасы'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, genre)
        collection.set_book_genre(first_book, new_genre)
        assert collection.get_book_genre(first_book) == new_genre

    def test_set_book_genre_absent_genre_not_added(self, collection):
        first_book = 'Властелин колец'
        absent_genre = 'Научная литература'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, absent_genre)
        assert collection.get_book_genre(first_book) == ''

    def test_get_books_with_specific_genre_success(self, collection_five_books):
        assert collection_five_books.get_books_with_specific_genre('Ужасы') == ['Дракула']

    def test_get_books_with_specific_genre_absent_book(self, collection_five_books):
        assert len(collection_five_books.get_books_with_specific_genre('Лечебная литература')) == 0

    def test_get_books_for_children_success(self, collection_five_books):
        children_books = collection_five_books.get_books_for_children()
        assert len(children_books) == 3 and children_books == ['Властелин колец', 'Незнайка на Луне', '12 стульев']

    def test_add_book_in_favorites_add_one_book_added(self, collection):
        first_book = 'Капитал'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book

    def test_add_book_in_favorites_add_absend_book_not_added(self, collection):
        first_book = 'Властелтин колец'
        collection.add_book_in_favorites(first_book)
        assert len(collection.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_add_repeated_book_not_added(self, collection):
        first_book = 'Оно'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.add_book_in_favorites(first_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book

    def test_delete_book_from_favorites_book_delete(seld, collection):
        first_book = 'Князь серебрянный'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.delete_book_from_favorites(first_book)
        assert len(collection.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_absent_book_delete(seld, collection):
        first_book = 'Князь серебрянный'
        second_book = 'Сияние'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.delete_book_from_favorites(second_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book