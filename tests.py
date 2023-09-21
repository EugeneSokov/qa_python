import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_three_books(self):

        collector = BooksCollector()

        collector.add_new_book('Я')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 3

    def test_add_new_book_add_zero_books(self):

        collector = BooksCollector()

        collector.add_new_book('')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить?')

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_genre_added(self):

        genre = BooksCollector()
        book_name = 'Убийство в восточном экспрессе'
        genre.add_new_book(book_name)
        genre.set_book_genre(book_name, 'Детективы')

        assert genre.get_book_genre(book_name) == 'Детективы'

    def test_set_book_genre_genre_not_added(self):
            genre = BooksCollector()
            book_name = 'Евгений Онегин'
            genre.add_new_book(book_name)
            genre.set_book_genre(book_name, 'Поэмы')

            assert genre.get_book_genre(book_name) == ''
    def test_get_book_genre_genre_from_list(self):

        genre = BooksCollector()
        book_name = 'Путешествие к центру Земли'
        genre.add_new_book(book_name)
        genre.set_book_genre(book_name, 'Фантастика')

        assert genre.get_book_genre(book_name) == 'Фантастика'

    @pytest.mark.parametrize('book_name,genre',
                              [
                              ['Book1', 'Фантастика'],
                              ['Book2', 'Ужасы'],
                              ['Book3', 'Детективы'],
                              ['Book4', 'Мультфильмы'],
                              ['Book5', 'Комедии']
                             ]
                             )
    def test_get_books_with_specific_genre_genres_from_list_received(self, book_name, genre):
        book = BooksCollector()
        book.add_new_book(book_name)
        book.set_book_genre(book_name, genre)
        assert book.get_books_with_specific_genre(genre)[0] == book_name

    def test_get_books_with_specific_genre_genres_not_from_list_rejected(self):
            book = BooksCollector()
            book_name = 'Властелин колец'
            genre  = 'Фэнтези'
            book.add_new_book(book_name)
            book.set_book_genre(book_name, genre)
            assert len(book.get_books_with_specific_genre(genre)) == 0

    def test_get_books_for_children_different_age_rating_genres_received_child_books(self):
            child_book = BooksCollector()
            child_book.add_new_book('ChildBook1')
            child_book.add_new_book('AdultBook1')
            child_book.set_book_genre('ChildBook1', 'Мультфильмы')
            child_book.set_book_genre('AdultBook1', 'Ужасы')
            assert len(child_book.get_books_for_children()) == 1

    def test_add_book_in_favorites_add_new_book_received(self):
        favorite_book = BooksCollector()
        book_name = 'Моя любимая книга'
        favorite_book.add_new_book(book_name)
        favorite_book.add_book_in_favorites(book_name)
        assert favorite_book.get_list_of_favorites_books()[0] == book_name

    def test_add_book_in_favorites_add_new_book_not_from_list_rejected(self):
            favorite_book = BooksCollector()
            book_name = 'Моя любимая книга'
            favorite_book.add_book_in_favorites(book_name)
            assert len(favorite_book.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_add_existing_book_rejected(self):
            favorite_book = BooksCollector()
            book_name = 'Моя любимая книга'
            favorite_book.add_new_book(book_name)
            favorite_book.add_book_in_favorites(book_name)
            favorite_book.add_book_in_favorites(book_name)
            assert len(favorite_book.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_book_deleted(self):
                favorite_book = BooksCollector()
                book_name = 'Моя любимая книга'
                favorite_book.add_new_book(book_name)
                favorite_book.add_book_in_favorites(book_name)
                favorite_book.delete_book_from_favorites(book_name)
                assert len(favorite_book.get_list_of_favorites_books()) == 0

