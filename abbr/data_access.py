PAYMENT_TABLE = 'payments'

class PaymentDao:
    def __init__(self, initial_value: int = 0):
        self._storage = { PAYMENT_TABLE: initial_value }

    def retrieve(self) -> int:
        return self._storage[PAYMENT_TABLE]

    def save(self, payment: int) -> None:
        self._storage[PAYMENT_TABLE] = payment
