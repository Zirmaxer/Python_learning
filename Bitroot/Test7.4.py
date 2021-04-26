'''
Напишіть структуру класів, яка реалізує бібліотеку.
Класи:
Library – name, books = set(), authors = set()
Book – name, year, author (author має бути екземпляром класу Author)
Author – name, country, birthday, books = set()
Методи класу Author:
write_new_book(name: str, year: int) – повертає екземпляр класу Book і додає книгу до
списку книг автора
Методи класу Library:
add_new_book(book: Book) – додає книгу до списку книг поточної бібліотеки
group_by_author(author: Author) – повертає список усіх книг за заданим автором.
group_by_year(year: int) – повертає список усіх книг за заданим роком.
Усі три класи повинні мати читабельні методи __repr__ та __str__. Також клас Book повинен
мати змінну класу books_count, в якій зберігається кількість усіх наявних книг. Усі книги мають
бути унікальними.
class Library:
    pass
class Book:
    pass
class Author:
    pass
'''



class Author:
    def __init__(self, name, country, birthday, books=None):
        self.name = name
        self.country = country
        self. birthday = birthday
        if books is None:
            self.books = set()
        else:
            self.books = books

    def __str__(self):
        return f'Author is named {self.name} from {self.country}, who was born in {self.birthday} and writ those books:{self.books}'
    def __repr__(self):
        return f'Author={self.name}, country={self.country}, birthday={self.birthday}, books={self.books}'

    def write_new_book(self, name: str, year: int):
        if not isinstance(name, str):
            raise ValueError('name must be str')
        if not isinstance(year, int):
            raise ValueError('year must be int')
        book = Book(name, year, self)
        print (book)
        if book in self.books:
            pass
        else:
            Book.books_count += 1
            self.books.add(book)
            return book


class Book:
    books_count = 0
    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
#        if not isinstance(author, Author):
#            raise ValueError('Author must be member of class Author')
        self.author = author
        self.number = Book.books_count

    def __str__(self):
        return f'Book name is {self.name}, writen in {self.year} by {self.author}'
    def __repr__(self):
        return f'Book={self.name}, year={self.year}, author={self.author}'
    def __eq__(self, other):
        return self.name == other.name and self.year == other.year and self.author == other.author
    def __hash__(self):
        return hash(tuple([self.name, self.year, self.author]))


class Library:
    def __init__(self, name, books=None, authors=None ):
        self.name = name
        if books is None:
            self.books = set()
        else:
            self.books = books
        if authors is None:
            self.authors = set()
        else:
            self.authors = authors

    def __repr__(self):
        return f'Library named {self.name} had books:{self.books} of those authors: {self.authors}'

    def __str__(self):
        return f'Library named {self.name} had books:{self.books} of those authors: {self.authors}'

    def add_new_book(self, book: Book):
        self.books.add(book)

    def group_by_author(self, author: Author):
        if not isinstance(author, Author):
            raise ValueError('Author must be member of class Author' )
        pass

    def group_by_year(self, year: int):
        if not isinstance(year, int):
            raise ValueError('year must be integer')
        pass




if __name__ == "__main__":
    Timtryazeva = Library('Timtryazeva', {'book1', 'book2', 'book3'}, {'King', 'Pushkin'})
    print(Timtryazeva)
    Timtryazeva.add_new_book('book4')
    print(Timtryazeva)
    King = Author('King', 'GB', '01.01.1900')
    print(King)
    King.write_new_book('Shine', 2000)
    King.write_new_book('IT', 1990)
    print(Book.books_count)


