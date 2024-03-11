from data_access import PaymentDao


class PaymentProcessor:
    def __init__(self):
        self._dao = PaymentDao()

    def get_payment(self):
        return self._dao.retrieve()

    payment = property(get_payment)

    def is_payment_made(self):
        payment = self._dao.retrieve()
        return payment >=4

    def make_payment(self, coins):
        self._dao.save(coins)
