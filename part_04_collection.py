# Name: Muhammad Khalil
# Roll Number: TRN-2026-000376
# Date: 10-11-2026

# Shopping List Program
print("==========Shopping List==========")

# Create a shopping list
shopping_list = ["milk", "bread", "eggs"]

# Add a new item to the list
shopping_list.append("tea")

# Remove an item from the list
shopping_list.remove("bread")

# Sort the shopping list alphabetically
shopping_list.sort()

# Display items with serial numbers using enumerate()
for number, items in enumerate(shopping_list,start = 1):
    print(f"{number}. {items}")

print("===================================")   


# Phone Book Program
print()
print("==========Phone Book==========")

# Create a dictionary to store contact names and phone numbers
contacts = {
    "Ali": "03001234567",
    "Sara": "03111234567",
    "Ahmed": "03451234567",
    "Kamal": "03451234567",
    "Khalil": "03471234567"
}

# Keep the phone book menu running until the user exits
while True:

    # Display available phone book options
    print("\n1 = Add Contact")
    print("2 = Search Contact")
    print("3 = Delete Contact")
    print("4 = Show All Contacts")
    print("5 = Exit")

    # Get the user's choice
    user = input("Enter your choice: ")

    # Add a new contact to the dictionary
    if user == "1":
        contact_name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")

        contacts[contact_name] = phone_number
        print("Contact added successfully!")

    # Search for a contact using its name
    elif user == "2":
        contact_name = input("Enter name to search: ")

        # Get the phone number using the dictionary get() method
        number = contacts.get(contact_name)

        if number:
            print(f"{contact_name}: {number}")
        else:
            print("Not found!")

    # Delete a contact from the dictionary
    elif user == "3":
        contact_name = input("Enter name to delete: ")

        # Check if the contact exists before deleting
        if contact_name in contacts:
            del contacts[contact_name]
            print("Contact deleted successfully!")
        else:
            print("Not found!")

    # Display all saved contacts
    elif user == "4":
        print("\n========== All Contacts ==========")

        # Loop through dictionary items
        for name, number in contacts.items():
            print(f"{name}: {number}")

    # Exit the phone book program
    elif user == "5":
        print("Phone Book Closed!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice!")




# Class Result Sheet Program
print("========== Class Result Sheet ==========")

# Store student names and their marks in a dictionary
students = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [35, 65, 70],
    "Kamal": [55, 30, 80],
    "Khalil": [85, 90, 95]
}

# Initialize variables for finding the class topper
topper = ""
highest_total = 0

# Create an empty set to store students with marks below 40
below_40 = set()

# Loop through each student's name and marks
for name, marks in students.items():

    # Calculate total and average marks
    total = sum(marks)
    average = total / 3

    # Display each student's result
    print(f"\nStudent: {name}")
    print(f"Total Marks: {total}")
    print(f"Average: {average:.2f}")

    # Find the student with the highest total marks
    if total > highest_total:
        highest_total = total
        topper = name

    # Check each subject mark for values below 40
    for mark in marks:
        if mark < 40:
            below_40.add(name)

# Display the class topper and highest total marks
print("\n========== Class Topper ==========")
print(f"Topper: {topper}")
print(f"Highest Total: {highest_total}")

# Display students who scored below 40 in any subject
print("\n========== Students Below 40 ==========")
print(below_40)