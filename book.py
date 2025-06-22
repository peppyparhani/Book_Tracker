from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, genre, date_finished, rating):
        self.title = title
        self.author = author
        self.genre = genre
        self.date_finished = date_finished
        self.rating = rating
    
    @abstractmethod
    def book_type (self):
        pass

    def to_dict (self):
        return {
            'type' : self.book_type(),
            'title' : self.title,
            'author' : self.author,
            'genre' : self.genre,
            'date_finished' : self.date_finished,
            'rating' : self.rating
        }

class Novel(Book) :
    def book_type(self):
        return "📘 Novel"

class NonFiction(Book) :
    def book_type(self):
        return "📗 Non-Fiksi"