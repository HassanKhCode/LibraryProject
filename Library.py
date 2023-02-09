from datetime import datetime
from abc import ABC, abstractmethod

from Customer import Customer


class Library:
    def add_customer(self, id: int, name: str, address: str,
                 email: str, birth_date: datetime):
        customer = Customer(id, name, address, email, birth_date)
