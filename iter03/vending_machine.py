from enum import Enum

class Coin(Enum):
    PENNY = 'penny'  # Not acceptable
    NICKEL = 'nickel'
    DIME = 'dime'
    QUARTER = 'quarter'

# Messages
INSERT_COIN = 'INSERT COIN' # when no coins inserted
THANK_YOU = 'THANK YOU'     # after product dispensed


class VendingMachine:
    def __init__(self):
        self._total_amount = 0
        self.nickels = 0
        self.dimes = 0
        self.quarters = 0
        self.rejects = 0
        self._display = INSERT_COIN

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

    def select_cola(self):
        dispense = {}

        if self._total_amount >= 1.00:
            dispense['cola'] = 1
            self._total_amount -= 1.00
            self.display = THANK_YOU
        else:
            self.display = 'PRICE $1.00'

        return dispense
