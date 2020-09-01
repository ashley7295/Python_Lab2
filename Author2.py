
class Author:
    def __init__ (self, name):
        self.name = name
        self.books = []
    
    def publish (self, title):
        #adds an if statement before appending the book to see if it is already in the books list
        if title in self.books:
            print ("this title has already been published")
        else: 
            self.books.append(title)

    #joins the list of books to a new variable and returns a nicely formatted print
    def __str__ (self):
        list_of_books =', '.join(self.books)
        return f'Author: {self.name}, Here are the books they have written: {list_of_books}'


sanderson = Author('Brandon Sanderson')

#inital start ao ask the user for an input
new_book = input('Please Enter a book to publish: ')

#adds that book to the published books
sanderson.publish(new_book)

#binary for the while loop
questions = True

#while loop to keep asking the user if they would like to add a book to the list of publisehd books
while questions:

    #asks the user to continue with a "y" or "n"
    keep_adding = input('Do you want to add another book?(y/n):')

    #if the user enters "y", ask them to add another book and add it to the lsit of publisehd books
    if keep_adding == "y":
        new_book = input('Please Enter a book to publish: ')
        sanderson.publish(new_book)
    #if the user enters anything other than "y" it will end the loop
    else:
        questions = False

#prints the authors information
print(sanderson)