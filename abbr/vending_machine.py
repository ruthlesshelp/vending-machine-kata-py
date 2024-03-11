from payment_processor import PaymentProcessor

class VendingMachine:
    def __init__(self):
        self._payment = PaymentProcessor()
        self._quarters = 0
        self.display = 'THANK YOU'

    def release_quarters(self):
        quarters = self._quarters
        self._quarters = 0
        return quarters

    def  insert_quarters(self, quarters):
        self._quarters += quarters
        self._payment.make_payment(quarters * 25)

    def select_product(self):
        if self._payment.is_payment_made():
            self._quarters -= 4
            return 1
        raise RuntimeError
