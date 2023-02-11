import datetime


class Book:
    def __init__(self, id: int, name: str, author: str,
                 published_year: datetime, type: int):
        self.__id: int = id
        self.__name: str = name
        self.__author: str = author
        self.__published_year: datetime = published_year
        self.__type: int = type

    def get_book_id(self):
        return self.__id

    def get_book_name(self):
        return self.__name

    def get_book_author(self):
        return self.__author

    def get_book_published_year(self):
        return self.__published_year

    def get_book_type(self):
        return self.__type

    def get_loan_type(self):
        return self.__type

    def set_loan_type(self, type: int):
        self.__type = type