from datetime import datetime


class Loan:
    def __init__(self, customer_id: int, book_id: int,
                 loan_date: datetime, return_date: datetime):
        self.__customer_id: int = customer_id
        self.__book_id: int = book_id
        self.__loan_date: datetime = loan_date
        self.__return_date: datetime = return_date
