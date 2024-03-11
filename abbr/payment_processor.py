class PaymentProcessor:
    def __init__(self):
        self.payment = 0

    def is_payment_made(self):
        return self.payment >=4

    def make_payment(self, coins):
        self.payment = coins
