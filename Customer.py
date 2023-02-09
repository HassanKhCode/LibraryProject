from datetime import datetime


class Customer:
    def __init__(self, id: int, name: str, address: str,
                 email: str, birth_date: datetime):
        self.__id: int = id
        self.__name: str = name
        self.__address: str = address
        self.__email: str = email
        self.__birth_date: datetime = birth_date
