from datetime import datetime
import Library


class Book(Library):
    def __init__(self, id: int, name: str, author: str,
                 published_year: datetime, type: int):
        self.__id: int = id
        self.__name: str = name
        self.__author: str = author
        self.__published_year: datetime = published_year
        self.__type: int = type
