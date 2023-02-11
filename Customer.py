import datetime


class Customer:
    def __init__(self, id: int, name: str, address: str,
                 email: str, birth_date: datetime):
        self.__id: int = id
        self.__name: str = name
        self.__address: str = address
        self.__email: str = email
        self.__birth_date: datetime = birth_date

    def get_customer_id(self):
        return self.__id

    def get_customer_name(self):
        return self.__name

    def get_customer_address(self):
        return self.__address

    def get_customer_email(self):
        return self.__email

    def get_customer_birthdate(self):
        return self.__birth_date

