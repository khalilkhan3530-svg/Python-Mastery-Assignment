# Name: Muhammad Khalil
# Roll Number: TRN-2026-000376
# Date: 10-11-2026

print("==========References and Mutability==========")

# Task 1: Predict, then run

# Example 1
a = [1, 2, 3]
b = a

# Prediction: Both variables will show the same updated list
b.append(4)

print(a)


# Example 2
c = a.copy()
c.append(5)

# Prediction: Only c will change
print(a, c)


# Example 3
# Prediction: True, False, True
print(a is b, a is c, a == a[:])


print("==========End of Task 1==========")


print("==========Fix the Cart Bug==========")

# Buggy function: The same list is shared between calls
def add_item(item, cart=[]):
    cart.append(item)
    return cart

# Two calls show the shared list bug
print(add_item("Apple"))
print(add_item("Banana"))


# Fixed function: Create a new list when cart is None
def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart

# Two calls now use separate lists
print(add_item_fixed("Apple"))
print(add_item_fixed("Banana"))


print("==========End of Task 2==========")


print("==========Safe Class Copy==========")

import copy

# Original dictionary
classes = {
    "A": ["Ali", "Sara"]
}

# Create shallow copy and deep copy
shallow_copy = copy.copy(classes)
deep_copy = copy.deepcopy(classes)

# Add a student through shallow copy
shallow_copy["A"].append("Ahmed")

# Add a student through deep copy
deep_copy["A"].append("Hassan")

# Print all three dictionaries
print("Original:", classes)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)

print("==========End of Task 3==========")