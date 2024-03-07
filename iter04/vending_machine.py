# vending_machine.py

from enum import Enum

class Coin(Enum):
    PENNY = 'penny'  # Not acceptable
    NICKEL = 'nickel'
    DIME = 'dime'
    QUARTER = 'quarter'

class Product(Enum):
    COLA = 'cola'
    CHIPS = 'chips'
    CANDY = 'candy'

# Messages
INSERT_COIN = 'INSERT COIN' # when no coins inserted
THANK_YOU = 'THANK YOU'     # after product dispensed


class VendingMachine:
    # prices for each product
    _prices = { Product.COLA: 1.00, Product.CHIPS: 0.50, Product.CANDY: 0.65 }

    def __init__(self):
        # time.sleep(2) # Use a 2 sec sleep to simulate a long initialization.
        self._reset()

    # properties
    def get_display(self):
        current_display = self._display

        if self._display == THANK_YOU:
            self._display = INSERT_COIN

        if self._display == 'PRICE $1.00':
            self._display = INSERT_COIN

        return current_display
    
    def set_display(self, display):
        self._display = display

    display = property(get_display, set_display)

    def get_current_amount(self):
        return f'${self._total_amount:.2f}'

    def set_current_amount(self):
        pass

    current_amount = property(get_current_amount, set_current_amount)

    # methods
    def return_coins(self):
        self.display = INSERT_COIN
        return_slot = {}
        if self.nickels > 0:
            return_slot['nickels'] = self.nickels
        if self.dimes > 0:
            return_slot['dimes'] = self.dimes
        if self.quarters > 0:
            return_slot['quarters'] = self.quarters
        if self.rejects > 0:
            return_slot['rejects'] = self.rejects

        return return_slot

    def insert_coins(self, coin_type: Coin, coins: int):
        amount = 0
        if coin_type == Coin.QUARTER:
            self.quarters += coins
            amount = coins * 0.25
        elif coin_type == Coin.NICKEL:
            self.nickels += coins
            amount = coins * 0.05
        elif coin_type == Coin.DIME:
            self.dimes += coins
            amount = coins * 0.10
        else:
            self.rejects += coins

        self._total_amount += amount
        self.display = self.current_amount

    def select_product(self, product: Product):
        dispense = {}
        price = self._prices[product]

        if self._total_amount >= price:
            dispense[product.value] = 1
            self._total_amount -= price
            self.display = THANK_YOU
        else:
            self.display = f'PRICE ${price:.2f}'

        return dispense

    # private testability enhancement
    def _reset(self):
        self._total_amount = 0
        self.nickels = 0
        self.dimes = 0
        self.quarters = 0
        self.rejects = 0
        self._display = INSERT_COIN
