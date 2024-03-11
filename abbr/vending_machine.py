from payment_processor import PaymentProcessor

class VendingMachine:
    def __init__(self):
        self._payment = PaymentProcessor()
        self.display = 'THANK YOU'

    def release_payment(self):
        return self._payment.payment

    def  insert_payment(self, quarters):
        self._payment.make_payment(quarters)

    def select_product(self):
        if self._payment.is_payment_made():
            return 1
        raise RuntimeError
