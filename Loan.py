import datetime


def max_loan_time(loan_type: int) -> datetime:
    if loan_type == 1:
        max_time = datetime.timedelta(days=10)
    elif loan_type == 2:
        max_time = datetime.timedelta(days=5)
    else:
        max_time = datetime.timedelta(days=2)
    return max_time


class Loan:
    def __init__(self, customer_id: int, book_id: int,
                 loan_date: datetime, loan_type: int, return_date: datetime = None):
        self.__customer_id: int = customer_id
        self.__book_id: int = book_id
        self.__loan_date: datetime = loan_date
        self.__return_date = return_date
        self.__max_return_date: datetime = loan_date + max_loan_time(loan_type)

    def get_loan_date(self):
        return self.__loan_date

    def get_return_date(self):
        return self.__return_date

    def set_loan_date(self, date: datetime):
        self.__loan_date = date

    def set_return_date(self, date: datetime):
        self.__return_date = date

    def get_max_return_date(self):
        return self.__max_return_date

