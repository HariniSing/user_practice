class User:


    def __init__(self,name):
        self.name = name
        self.amount = 0
        return self

    def make_withdrawal(self,amount):
        self.amount-= amount
        return self

    def make_deposits(self,amount):
        self.amount+= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount 
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

harini = User("Harini")
micheal = User("Micheal")
sheldon = User("Sheldon")

# 3 deposits and 1 withdrawal and then display their balance
harini.make_deposits(100).make_deposits(400).make_deposits(800).make_withdrawal(800).display_user_balance()

# make 2 deposits and 2 withdrawals
micheal.make_deposits(1400).make_deposits(1000).make_withdrawal(800).make_withdrawal(800).display_user_balance()

# 1 deposits and 3 withdrawals 
sheldon.make_deposits(1400).make_withdrawal(800).make_withdrawal(100).make_withdrawal(100).display_user_balance()

# Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
harini.transfer_money(300,sheldon)