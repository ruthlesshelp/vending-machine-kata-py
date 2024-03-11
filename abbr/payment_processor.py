from data_access import PaymentDao


class PaymentProcessor:
    def __init__(self):
        self._dao = PaymentDao()

    def get_payment(self):
        return self._dao.retrieve()

    def is_payment_made(self):
        payment = self.get_payment()
        return payment >= 100

    def make_payment(self, coins):
        self._dao.save(coins)
