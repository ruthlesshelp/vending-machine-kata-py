class VendingMachine:
    def __init__(self):
        self.coins = 0
        self.display = 'INSERT COIN'

    def return_coins(self):
        self.display = 'INSERT COIN'
        return self.coins
    
    def insert_coin(self, coins: int):
        amount = coins * 0.25
        self.display = f'${amount}'
        self.coins += coins