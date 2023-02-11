import datetime
from Customer import Customer
from Book import Book
from Loan import Loan


class Library:
    def __init__(self, name: str):
        self.__name: str = name
        self.__books: dict[int, Book] = {}
        self.__customers: dict[int, Customer] = {}
        self.__loans: dict[int, Loan] = {}
        self.__returned_loans: dict[int, list[Loan]] = {}
        self.__late_returned_loans: dict[int, list[Loan]] = {}

    def add_customer(self, id: int, name: str, address: str,
                 email: str, birth_date: datetime):
        if id in self.__customers:
            return "This customer is already registered!"
        new_customer = Customer(id, name, address, email, birth_date)
        self.__customers[id] = new_customer
        f"Welcome to our library {name}"

    def add_book(self, id: int, name: str, author: str,
                 published_year: datetime, type: int):
        if id in self.__books:
            return "We already have that book"
        new_book = Book(id, name, author, published_year, type)

    def loan_book(self, customer_id: int, book_id: int,
                 loan_date: datetime, loan_type: int):
        if customer_id in self.__loans:
            return "Sorry this book has already been loaned"
        new_loan = Loan(customer_id, book_id, loan_date, loan_type)

    def return_book(self, customer_id: int, book_id: int):
        if customer_id not in self.__loans:
            return "This book hasn't been loaned!"
        else:
            return_date = datetime.datetime.now()
            if self.__loans[customer_id].get_max_return_date() >= return_date:
                self.__returned_loans[customer_id].append(self.__loans[customer_id])
                self.__loans.pop(customer_id)
            else:
                self.__late_returned_loans[customer_id].append(self.__loans[customer_id])
                self.__loans.pop(customer_id)

    def display_all_books(self):
        books = []
        for v in self.__books.values():
            books.append(v)
        return books

    def display_all_customers(self):
        customers = []
        for v in self.__customers.values():
            customers.append(v)
        return customers

    def display_all_loans(self):
        loans = []
        for v in self.__loans.values():
            loans.append(v)
        return loans

    def display_all_late_loans(self):
        late_loans = []
        for v in self.__late_returned_loans.values():
            late_loans.append(v)
        return late_loans

    def display_customer_loans(self, id: int):
        return self.__loans[id]

    def find_book_with_name(self, name: str):
        for id, book in self.__books:
            if book.get_book_name() == name:
                return book.get_book_name()

    def find_book_with_author(self, author: str):
        for id, book in self.__books:
            if book.get_book_author() == author:
                return book.get_book_author()

    def remove_book_from_library(self, book_id: int):
        if book_id not in self.__books:
            return "This book doesn't exist"
        elif book_id in self.__loans:
            return "You need to return the book first!"
        elif book_id in self.__late_returned_loans:
            return "You need to return the book first!"
        else:
            self.__books.pop(book_id)

    def remove_customer_from_library(self, customer_id: int):
        if customer_id not in self.__customers:
            return "Unknown Customer"
        elif customer_id in self.__loans:
            return "Customer needs to return a book"
        elif customer_id in self.__late_returned_loans:
            return "Customer needs to return a book"
        else:
            self.__customers.pop(customer_id)
