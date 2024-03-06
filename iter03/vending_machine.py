from enum import Enum

class Coin(Enum):
    PENNY = 'penny'  # Not acceptable
    NICKEL = 'nickel'
    DIME = 'dime'
    QUARTER = 'quarter'

# Message when no coins
INSERT_COIN = 'INSERT COIN'


class VendingMachine:
    def __init__(self):
        self.total_amount = 0
        self.nickels = 0
        self.dimes = 0
        self.quarters = 0
        self.rejects = 0
        self.display = INSERT_COIN

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

        self.total_amount += amount
        self.display = f'${self.total_amount:.2f}'

    def select_cola(self):
        dispense = {}

        if self.total_amount >= 1.00:
            dispense['cola'] = 1
            self.display = 'THANK YOU'

        return dispense
