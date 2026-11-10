# Name: Muhammad Khalil
# Roll Number: TRN-2026-000376
# Date: 10-11-2026

# Positive, Negative, Zero and Even/Odd Number Checker

# Get a number from the user
number = int(input("Enter a number: "))

# Check whether the number is zero, positive or negative
if number == 0:
    print("Zero")
elif number > 0:
    print("Positive Number")       
else:
    print("Negative Number")        

# Check whether the number is even or odd
if number % 2 == 0:
    print("Even Number")
elif number %2 != 0:
    print("Odd Number")     


# Grade Calculator
print("===========Grade Culculator==========")
print()

# Get marks from the user
marks = int(input("Enter your marks: "))

# Check marks and assign a grade
if marks > 100 or marks < 0:
    print("Invalid marks!")    
elif marks >= 80:
    print("A Grade")
elif marks >= 70:
    print("B Grade")    
elif marks >= 60:
    print("C Grade")
elif marks >= 33:
    print("D GRade")
else:
    print("Fail")            

print()
print("======================================")    


# Electricity Bill Calculator
print("===========Elecricity Bill===========")
print()

# Get electricity units from the user
units = int(input("Enter Bill units: "))

# Set fixed charges
fixed_charges = 50

# Calculate bill according to electricity units
if units < 0:
    print("Invalid units!")

# Calculate bill for up to 100 units
elif units <= 100:
    print(f"Your total Bill price is: {units * 10 + fixed_charges}") 

# Calculate bill for 101 to 200 units
elif units <= 200:
    print(f"Your total Bill price is: {(units - 100)* 15 + 100*10 +fixed_charges}")

# Calculate bill for more than 200 units
else:
    print(f"Your total Bill price is: {(units - 200) * 20 + 100 * 15 + 100*10 + fixed_charges}")

print()
print("======================================")