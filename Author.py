
class Author:
    def __init__ (self, name):
        self.name = name
        self.books = []
    
    def publish (self, title):
        self.books.append(title)

    def __str__ (self):
        list_of_books = ", ".join(self.books)
        return f'Author: {self.name}, Here are the books they have written: {list_of_books}'


sanderson = Author('Brandon Sanderson')
sanderson.publish('Elantris')
sanderson.publish('Warbreaker')
sanderson.publish('Oathbringer')

print(sanderson)


