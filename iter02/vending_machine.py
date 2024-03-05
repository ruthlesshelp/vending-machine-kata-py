class VendingMachine:
    def __init__(self):
        self.nickels = 0
        self.dimes = 0
        self.coins = 0
        self.display = 'INSERT COIN'

    def return_coins(self):
        self.display = 'INSERT COIN'
        return self.coins

    def insert_coin(self, coins: int):
        amount = coins * 0.25
        self.display = f'${amount}'
        self.coins += coins

    def insert_nickel(self, coins: int):
        amount = coins * 0.05
        self.display = f'${amount}'
        self.nickels += coins

    def insert_dime(self, coins: int):
        self.dimes += coins
        self.display = '$0.10'