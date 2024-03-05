class VendingMachine:
    def __init__(self):
        self.coins = 0
        self.display = 'INSERT COIN'

    def release_change(self):
        return self.coins
    
    def insert_coin(self, coins: int):
        self.coins += coins