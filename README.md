# qa_python
В проекте используются следующие файлы:
conftest.py - вспомогательная функция - фикстура
main.py - класс BooksCollector
test.py - тестовый класс TestBooksCollector

В тестовом фале содержатся следующие методы(тесты):
test_add_new_book_add_two_books: Проверка добавления двух книг (исходный образец)
test_add_new_book_enable_default_genre_success: Проверка установления жанра по умолчанию в добавленной книге
test_add_new_book_with_incorrect_name_not_added: Негативная проверка добавления книг с именем 0 и больше 40 символов (параметризированный тест с двумя аргументами)
test_add_new_book_add_repeated_books_not_added: Негативная проверка повторного добавления одинаковых книг
test_set_book_genre_added: Проверка добавления жанра из списка genre книге из списка books_genre
test_set_book_genre_change: Проверка изменения жанра из списка genre книге из списка books_genre
test_set_book_genre_absent_genre_not_added: Негативная проверка добавления жанра не из списка genre книге из списка books_genre
test_get_books_with_specific_genre_success: Проверка вывода книги определенного жанра
test_get_books_with_specific_genre_absent_book: Негативная проверка вывода отсутствующей книги определенного жанра
test_get_books_for_children_success: Проверка вывода списка книг с жанром для детей
test_add_book_in_favorites_add_one_book_added: Проверка добавления книги из списка books_genre в избранное
test_add_book_in_favorites_add_absend_book_not_added: Негативная проверка добавления книги не из списка books_genre в избранное
test_add_book_in_favorites_add_repeated_book_not_added: Негативная проверка повторного добавления книги в избранное
test_delete_book_from_favorites_book_delete: Проверка удаления книги из списка избранное
test_delete_book_from_favorites_absent_book_delete: Негативная проверка удаления книги не из списка избранное