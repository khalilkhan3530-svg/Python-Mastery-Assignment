# Name: Muhammad Khalil
# Roll Number: TRN-2026-000376
# Date: 10-11-2026
# Student Card Program
print("===========Student Card==========")

# Get student information from the user
student_name = input("Enter Your Name: ")
student_age = int(input("Enter your age: "))
class_name = input("What class are you in: ")
city_name = input("Where City do yu live in: ")

# Display student information
print(f"Name\t: {student_name}")
print(f"Age \t: {student_age}")
print(f"Class\t: {class_name}")
print(f"City\t: {city_name}")
print()

# Display data types of variables
print(type(student_name))
print(type(student_age))
print(type(class_name))
print(type(city_name))
print()
print("===================================")


# Shop Bill Calculator
print("===========Shop Bill==========")
print()

# Get item details from the user
item_name = input("Enter items name: ")
item_price = float(input("Enter item price: "))
item_quantity =int(input("Enter items quantity: "))

# Calculate subtotal
sub_total = item_price*item_quantity

# Calculate 5% discount
discount = sub_total * 5 / 100
discounted_amount = sub_total-discount

# Calculate 17% tax
tax = (discounted_amount*17)/100

# Calculate final bill amount
total = discounted_amount + tax

# Display the complete bill
print(f"Item                : {item_name}")
print(f"Subtotal            : {sub_total:.2f}")
print(f"5% discount         : {discount:.2f}")
print(f"Discounted Amount   : {discounted_amount:.2f}")
print(f"17% Tax             : {tax:.2f}")
print(f"Total               : {total:.2f}")
print()
print("=================================")


# Unit Converter Program
print("==========Unit Converter==========")
print()

# Get temperature and distance from the user
temperature_in_celsius = float(input("Enter teperature in celsius: "))
distance_in_kilometer = float(input("Enter Distance in kilo meter: "))

# Convert Celsius to Fahrenheit and Kelvin
fahrenheit = (temperature_in_celsius * 9/5) + 32
kelvin = temperature_in_celsius + 273.15

# Convert kilometers to miles and meters
miles = distance_in_kilometer * 0.621371
meters = distance_in_kilometer* 1000

# Display all conversion results
print("Conversion  : result")
print(f"Fahrenheit  : {fahrenheit:.1f}")
print(f"Kelvin      : {kelvin:.1f}")
print(f"Miles       : {miles:.1f}")
print(f"meters      : {meters:.1f}")

print()
print("===================================")