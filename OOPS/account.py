class Account:

    def __init__(self, account_number, balance):
        self.__account_number = account_number 
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.__account_number}")

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debited {amount} from account {self.__account_number}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance
    
    def get_account_number(self):
        print(self.__account_number)

account1 = Account("1234567890", 5000)
account1.credit(2000)
account1.debit(1500)
print(account1.get_balance())
# account number is private (__account_number); use getter instead:

print(account1.get_account_number())


