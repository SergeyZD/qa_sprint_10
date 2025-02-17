import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize("book_name, expected", [
        ("Война и мир", True),
        ("123456789012345678901234567890123456789", True),  
        (" ", True),
        ("", False),
        ("12345678901234567890123456789012345678901", False)  
    ])
    def test_add_new_book(self, book_name, expected):
        collector = BooksCollector()
        result = collector.add_new_book(book_name)
        if expected:
            assert result is None
            assert book_name in collector.get_books_genre()
        else:
            assert result is None
            assert book_name not in collector.get_books_genre()

    @pytest.mark.parametrize("book_name, genre, expected_books", [
        ("Война и мир", "Фантастика", ["Война и мир"]),
        ("Преступление и наказание", "Ужасы", ["Преступление и наказание"]),
        ("Гарри Поттер", "Мультфильмы", ["Гарри Поттер"]),
        ("Война и мир", "Ужасы", ["Преступление и наказание"]), 
    ])
    def test_get_books_with_specific_genre(self, book_name, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        collector.add_new_book("Преступление и наказание")
        collector.set_book_genre("Преступление и наказание", "Ужасы")
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Мультфильмы")

        result = collector.get_books_with_specific_genre(genre)
        assert result == expected_books

    @pytest.mark.parametrize("book_name, genre", [
        ("Война и мир", "Несуществующий жанр"),
    ])
    def test_set_book_genre_invalid_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize("book_name, genre, expected_books", [
        ("Война и мир", "Фантастика", ["Война и мир"]),
        ("Преступление и наказание", "Ужасы", ["Преступление и наказание"]),
        ("Гарри Поттер", "Мультфильмы", ["Гарри Поттер"]),
        ("Война и мир", "Ужасы", ["Преступление и наказание"]),
    ])
    def test_get_books_with_specific_genre(self, book_name, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        collector.add_new_book("Преступление и наказание")
        collector.set_book_genre("Преступление и наказание", "Ужасы")
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Мультфильмы")

        result = collector.get_books_with_specific_genre(genre)
        print(f"Expected: {expected_books}, Actual: {result}")
        assert result == expected_books

    @pytest.mark.parametrize("book_name, genre, expected_books", [
        ("Война и мир", "Фантастика", ["Война и мир", "Гарри Поттер"]),
        ("Преступление и наказание", "Ужасы", ["Гарри Поттер"]),
        ("Гарри Поттер", "Мультфильмы", ["Война и мир", "Гарри Поттер"]),
    ])
    def test_get_books_for_children(self, book_name, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        collector.add_new_book("Преступление и наказание")
        collector.set_book_genre("Преступление и наказание", "Ужасы")
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Мультфильмы")
        expected = ['Война и мир', 'Гарри Поттер']
        assert collector.get_books_for_children() == expected

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        assert "Война и мир" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        assert collector.get_list_of_favorites_books() == ["Война и мир"]

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.delete_book_from_favorites("Война и мир")
        assert "Война и мир" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_in_favorites(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites("Война и мир")  
        assert not collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_with_books(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.add_new_book("Преступление и наказание")
        collector.add_book_in_favorites("Преступление и наказание")
        assert collector.get_list_of_favorites_books() == ["Война и мир", "Преступление и наказание"]