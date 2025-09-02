#programação Orientada a Objetos
class Library(object):
    def __init__(self, title, author, pub_year, call_no):
        self.title = title
        self.author = author
        self.pub_year = pub_year
        self.call_no = call_no
        self.checked_out = False

    def title_and_author(self):
        return "{} {}: {}".format(self.author[1], self.author[0], self.title)

    def __str__(self):
        return "{} {}({}): {}".format(self.author[1], self.author[0], self.pub_year, self.title)

    def __repr__(self):
        return "<book: {} ({})>".format(self.title, self.call_no)

# Criando e usando objetos fora da classe
my_book = Library("Dom Quixote", "Miguel de Cervantes", 1605, "123.456 CERV")
print("Título: " + my_book.title)
print("Autor: " + my_book.author)
print("Ano de publicação: " + str(my_book.pub_year))
print("Número de chamada: " + my_book.call_no)
print("Está emprestado? " + str(my_book.checked_out))

new_book = Library("Harry Potter and the Sorcerer's Stone", ("Rowling", "J.K."), 1998, "PZ7.R79835")
print(new_book.title_and_author())
print(new_book)