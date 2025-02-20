import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:

    @pytest.mark.parametrize("book_name", [
        "Война и мир", 
        "123456789012345678901234567890123456789", 
        " "
    ])
    def test_add_new_book_valid(self, collector, book_name):
        result = collector.add_new_book(book_name)
        assert result is None
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize("book_name", [
        "", 
        "12345678901234567890123456789012345678901"
    ])
    def test_add_new_book_invalid(self, collector, book_name):
        result = collector.add_new_book(book_name)
        assert result is None
        assert book_name not in collector.get_books_genre()

    @pytest.mark.parametrize("book_name, genre", [
        ("Война и мир", "Фантастика"),
        ("Преступление и наказание", "Ужасы"),
        ("Гарри Поттер", "Мультфильмы"),
    ])
    def test_set_book_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize("book_name, genre", [
        ("Война и мир", "Несуществующий жанр"),
    ])
    def test_set_book_genre_invalid_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize("genre, expected_books", [
        ("Фантастика", ["Война и мир"]),
        ("Ужасы", ["Преступление и наказание"]),
        ("Мультфильмы", ["Гарри Поттер"]),
    ])
    def test_get_books_with_specific_genre(self, collector, genre, expected_books):
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        collector.add_new_book("Преступление и наказание")
        collector.set_book_genre("Преступление и наказание", "Ужасы")
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Мультфильмы")

        result = collector.get_books_with_specific_genre(genre)
        assert result == expected_books

    @pytest.mark.parametrize("genre", [
        ("Несуществующий жанр"),
    ])
    def test_get_books_with_specific_genre_not_exist(self, collector, genre):
        result = collector.get_books_with_specific_genre(genre)
        assert result == []

    @pytest.mark.parametrize("expected_books", [
        (["Война и мир", "Гарри Поттер"]),
    ])
    def test_get_books_for_children(self, collector, expected_books):
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Мультфильмы")
        assert collector.get_books_for_children() == expected_books

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        assert "Война и мир" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self, collector):
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        assert collector.get_list_of_favorites_books() == ["Война и мир"]

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.delete_book_from_favorites("Война и мир")
        assert "Война и мир" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_in_favorites(self, collector):
        collector.delete_book_from_favorites("Война и мир")  
        assert not collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_with_books(self, collector):
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.add_new_book("Преступление и наказание")
        collector.add_book_in_favorites("Преступление и наказание")
        assert collector.get_list_of_favorites_books() == ["Война и мир", "Преступление и наказание"]