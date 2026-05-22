import pytest
from main import BooksCollector

@pytest.fixture()
def books():
    books = BooksCollector()
    books.add_new_book('Дюна')
    books.add_new_book('Шерлок Холмс')
    return books

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('books_invalid_length', ['', 'Книга длиною сорок один символ для теста!'])
    def test_add_new_book_add_invalid_length(self, books_invalid_length):
        collector = BooksCollector()
        collector.add_new_book(books_invalid_length)
        assert len(collector.get_books_genre()) == 0
    
    def test_set_book_genre_invalid_genre(self, books):
        books.set_book_genre('Дюна', 'Научная фантастика')
        assert books.get_book_genre('Дюна') == ''

    def test_set_book_genre_valid_genre_True(self, books):
        books.set_book_genre('Дюна', 'Фантастика')
        assert books.get_book_genre('Дюна') == 'Фантастика'

    def test_set_book_genre_for_not_existent_book(self, books):
        books.set_book_genre('1984', 'Ужасы')
        assert books.get_book_genre('1984') == ''

    def test_get_books_with_specific_genre_return_specific_books(self, books):
        books.set_book_genre('Дюна', 'Фантастика')
        books.set_book_genre('Шерлок Холмс', 'Детективы')
        assert len(books.get_books_with_specific_genre('Детективы')) == 1

    @pytest.mark.parametrize('books_names, genre_new_books', [
        ['Оно', 'Ужасы'], 
        ['Винни Пух', 'Мультфильмы'], 
        ['Бриллиантовая Рука', 'Комедии']
    ])
    def test_get_books_genre_added_book_has_correct_genre(self, books_names, genre_new_books):
        collector = BooksCollector() 
        collector.add_new_book(books_names)
        collector.set_book_genre(books_names, genre_new_books)
        assert collector.get_books_genre()[books_names] == genre_new_books

    def test_get_books_for_children_returns_only_children_books(self, books):
        books.set_book_genre('Дюна', 'Фантастика')
        books.set_book_genre('Шерлок Холмс', 'Детективы')
        assert books.get_books_for_children() == ['Дюна']

    def test_add_book_in_favorites_valid_books_add_True(self, books):
        books.set_book_genre('Дюна', 'Фантастика')
        books.set_book_genre('Шерлок Холмс', 'Детективы')
        books.add_book_in_favorites('Дюна')
        books.add_book_in_favorites('Шерлок Холмс')
        assert len(books.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_non_existent_book_False(self, books):
        books.add_book_in_favorites('1984')
        assert len(books.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_valid_book_removes_True(self, books):
        books.set_book_genre('Дюна', 'Фантастика')
        books.set_book_genre('Шерлок Холмс', 'Детективы')
        books.add_book_in_favorites('Дюна')
        books.add_book_in_favorites('Шерлок Холмс')
        books.delete_book_from_favorites('Дюна')
        assert books.get_list_of_favorites_books() == ['Шерлок Холмс']

