class VendingMachine:
    def __init__(self):
        self.coins = 0

    def release_change(self):
        return self.coins
    
    def insert_coin(self, coins: int):
        self.coins += coins