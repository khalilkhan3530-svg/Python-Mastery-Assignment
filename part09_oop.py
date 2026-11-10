# Name: Muhammad Khalil
# Roll Number: TRN-2026-000376
# Date: 10-11-2026

print("========== Student Class ==========")

class Student:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f"{self.name} (Roll {self.roll_number}): avg {self.average():.1f}"


# Create student object
student1 = Student("Ali", 12, [80, 75, 88])

print(student1)

# Add new mark
student1.add_mark(81)

print(student1)

print("===================================")



print("========== Bank Account ==========")

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        self.balance += amount
        self.history.append(f"Deposited: Rs {amount}")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        self.history.append(f"Withdrawn: Rs {amount}")

    def show_history(self):
        print("Transaction History:")

        for transaction in self.history:
            print(transaction)


# Create bank account
account = BankAccount("Ali", 1000)

# Perform transactions
account.deposit(500)
account.withdraw(200)

print("Owner:", account.owner)
print("Current Balance:", account.balance)

account.show_history()

print("==================================")



print("========== Bank Account ==========")

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        self.balance += amount
        self.history.append(f"Deposited: Rs {amount}")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        self.history.append(f"Withdrawn: Rs {amount}")

    def show_history(self):
        print("Transaction History:")

        for transaction in self.history:
            print(transaction)


# Create bank account
account = BankAccount("Ali", 1000)

# Perform transactions
account.deposit(500)
account.withdraw(200)

print("Owner:", account.owner)
print("Current Balance:", account.balance)

account.show_history()

print("==================================")
