class Atm():
    def __init__(self,cardnum,pin):
        self.carnum=cardnum
        self.pin=pin
    
    def check_balance(self):
        print("ur balance is 100000000$")

    def withdrawl(self,amount):
        newamount=100000000-amount
        print(newamount)