import pickle

class account:
        def __init__(self, id, balance):
                self.id = id
                self.balance = balance
        def deposit(self, amount):
                self.balance += amount
        def withdraw(self, amount):
                self.balance -= amount

my_account = account('00123', 1000)
my_account.deposit(700)
my_account.withdraw(400)

fd = open( "archive", "w" )
pickle.dump( my_account, fd)
fd.close()

my_account.deposit(500)
print my_account.balance,

fd = open( "archive", "r" )
my_account = pickle.load( fd )
fd.close()

print my_account.balance
