class VendingMachine:
    def __init__(self):
        self._payment = 0

    def release_payment(self):
        return self._payment

    def  insert_payment(self, quarters):
        self._payment = quarters

    def select_product(self):
        if self._payment >= 4:
            return 1
        raise RuntimeError
