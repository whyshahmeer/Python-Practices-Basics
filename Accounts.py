class BankAccount:
    def __init__(self):
        self.name = "Lighter" 
        self._balance = 1000 
        self.__pin = 1234 

    def get_pin(self):
        return "access denied"

    def set_pin(self, old_pin,new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("Pin updated")
        else:
            print("Wrong pin")
acc = BankAccount()
print(acc.name)
print(acc._balance)
acc.set_pin(1234, 5678)

acc = 


