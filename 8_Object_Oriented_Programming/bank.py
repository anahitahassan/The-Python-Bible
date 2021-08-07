# 70: Project 11: Bank

class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: {}".format(self.balance))

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

x = Current("Ziyad", 500)
x.deposit(300)
print(x.statement())
x.withdraw(1000)
print(x.statement())
x.withdraw(1000)
print(x.statement())

# 72: Section Review
#   - Classes are templates for objects
#   - Objects have states and methods
#   - You can access states with . index
#   - You can access methods with ()
#   - In order to have class methods you need __init__(self) constructor
#   - Use __del__(self) destructor to spend coins. (gets rid of a class)
#   - Inheritance in OOP (a parent class and a child class)
#   - Polymorphism -- override some behavior
#   - Use __str__(self) method to give nice output when printing
#   - 
#   - 
#   - 