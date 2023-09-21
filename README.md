# qa_python
# Список тестовых методов в tests.py и что они проверяют:

test_add_new_book_add_three_books - проверка добавления трёх книг в словарь, удовлетворяющих условию метода add_new_book()
test_add_new_book_add_zero_books - проверка отклонения в добавлении двух книг, которые не удовлетворяют условию метода add_new_book()
test_set_book_genre_genre_added - проверка установки жанра книге с жанром, удовлетворяющем условию метода set_book_genre()
test_set_book_genre_genre_not_added - проверка отклонения в установке жанра книги с жанром, который не удовлетворяет условию метода set_book_genre()
test_get_book_genre_genre_from_list - проверка получения жанра книги по ее имени
test_get_books_with_specific_genre_genres_from_list_received - проверка вывода списка книг с определённым жанром, удовлетворяющем условию метода get_books_with_specific_genre()
test_get_books_with_specific_genre_genres_not_from_list_rejected  -  проверка  отклонения  добавления книг в  список books_with_specific_genre, которые не удовлетворяют условию метода  get_books_with_specific_genre() по жанру
test_get_books_for_children_different_age_rating_genres_received_child_books - проверка вывода списка книг для детей, которые удовлетворят условию метода get_books_for_children()
test_add_book_in_favorites_add_new_book_received - проверка добавления книги в избранное, которая удовлетворяет условию метода add_book_in_favorites()
test_add_book_in_favorites_add_new_book_not_from_list_rejected - проверка отклонения добавления книги в избранное, которая отсутствует в словаре books_genre
test_add_book_in_favorites_add_existing_book_rejected - проверка отклонения повторного добавления книги в избранное
test_delete_book_from_favorites_delete_book_deleted - проверка удаления книги из списка "избранное", которая удовлетворяет условию метода delete_book_from_favorites()