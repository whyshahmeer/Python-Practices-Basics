class BadBankAccount:
        def_init__(self, balance):
        self.balance = balance

        account BadBankAccount(0.0)
        account.balance = -1
        print(account.balance)
        
class BankAccount:
        def_init__(self):
            self._balance = 0.0
            
        @property
        def balance(self):
            return self._balance

        def deposit(self):
            return self._balance
        
        def deposit(self, amount): 
            if amount <= 0:
                raise ValueError("Deposit must be positive")
            self._balance += amount
            
            def withdraw(self, amount):
                if amount <= 0:
            raise ValueError("Deposit amount must be positive")
                if amount >= self._balance:
                    raise ValueError("Insuffiecent funds")
                self.balance -= amount 
                
account = Bankaccounts()
print(account.balance)
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)
print()
