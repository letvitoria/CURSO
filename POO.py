#programação Orientada a Objetos
class Library(object):
    def __init__(self, title, author, pub_year, call_no):
        self.title = title
        self.author = author
        self.pub_year = pub_year
        self.call_no = call_no
        self.checked_out = False

my_book = Library("", "", 0, "")
my_book.title = "Dom Quixote"
my_book.author = "Miguel de Cervantes"
my_book.pub_year = 1605
my_book.call_no = "123.456 CERV"
my_book.checked_out = False

print("Título: " + my_book.title)
print("Autor: " + my_book.author)
print("Ano de publicação: " + str(my_book.pub_year))
print("Número de chamada: " + my_book.call_no)
print("Está emprestado? " + str(my_book.checked_out))