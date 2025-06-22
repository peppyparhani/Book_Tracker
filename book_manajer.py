import json
from book import Novel, NonFiction

class BookManager :
    def __init__(self, file_path="books.json"):
        self.file_path = file_path
        self.books = []
        self.load_books()
    
    def add_book (self, book) :
        self.books.append(book)
        self.save_books()
    
    def remove_book (self, index):
        if 0 <= index < len (self.books) :
            del self.books[index]
            self.save_books()

    def save_books (self) :
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4, ensure_ascii=False)

    def load_books(self) :
        try :
            with open (self.file_path, 'r', encoding='utf-8') as f :
                data = json.load(f)
                for b in data :
                    if b ['type'] == "📘 Novel":
                        book = Novel(b['title'], b['author'], b['genre'], b['date_finished'], b['rating'])
                    else :
                        book = NonFiction(b['title'], b['author'], b['genre'], b['date_finished'], b['rating'])
                    self.books.append(book)
        except FileNotFoundError :
            self.books = []
    
    def get_books (self) :
        return self.books