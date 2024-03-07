# vending_machine.py

import math

from enum import Enum

class CoinName(Enum):
    REJECT = 'reject' # Not acceptable
    PENNY = 'penny'   # Not acceptable
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

    def __init__(self, stock):
        # time.sleep(2) # Use a 2 sec sleep to simulate a long initialization.
        self._reset()
        self._stock = stock

    # properties
    def get_display(self):
        current_display = self._display

        if self._display == 'SOLD OUT':
            if self._total_amount > 0:
                self._display = f'${self._total_amount:.2f}'
            else:
                self._display = INSERT_COIN

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
    def return_coins(self) -> None:
        self.display = INSERT_COIN
        coin_return = {}
        if self.nickels > 0:
            coin_return[CoinName.NICKEL.value] = self.nickels
        if self.dimes > 0:
            coin_return[CoinName.DIME.value] = self.dimes
        if self.quarters > 0:
            coin_return[CoinName.QUARTER.value] = self.quarters
        if self.rejects > 0:
            coin_return[CoinName.REJECT.value] = self.rejects

        self.coin_return = coin_return

    def insert_coins(self, coin_type: CoinName, coins: int):
        amount = 0
        if coin_type == CoinName.QUARTER:
            self.quarters += coins
            amount = coins * 0.25
        elif coin_type == CoinName.NICKEL:
            self.nickels += coins
            amount = coins * 0.05
        elif coin_type == CoinName.DIME:
            self.dimes += coins
            amount = coins * 0.10
        else:
            self.rejects += coins

        self._total_amount += amount
        self.display = self.current_amount

    def select_product(self, product: Product) -> None:
        dispense = {}

        if self._stock[product.value] == 0:
            self.display = 'SOLD OUT'
            return

        price = self._prices[product]

        if self._total_amount >= price:
            dispense[product.value] = 1
            self._total_amount -= price
            self.coin_return = self._make_change()
            self.display = THANK_YOU
        else:
            self.display = f'PRICE ${price:.2f}'

        self.output_box = dispense

    def _make_change(self):
        coin_return = {}
        total_cents = math.ceil(self._total_amount * 100.0)

        quarters = int(total_cents / 25)
        if quarters > 0:
            coin_return[CoinName.QUARTER.value] = quarters
        total_cents -= quarters * 25

        dimes = int(total_cents / 10)
        if dimes > 0:
            coin_return[CoinName.DIME.value] = dimes
        total_cents -= dimes * 10

        nickels = int(total_cents / 5)
        if nickels > 0:
            coin_return[CoinName.NICKEL.value] = nickels
        total_cents -= nickels * 5

        return coin_return

    # private testability enhancement
    def _reset(self):
        self._total_amount = 0
        self.nickels = 0
        self.dimes = 0
        self.quarters = 0
        self.rejects = 0
        self.coin_return = {}
        self.output_box = {}
        self._display = INSERT_COIN
