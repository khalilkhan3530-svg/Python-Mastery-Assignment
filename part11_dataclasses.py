# Name: Muhammad Khalil
# Roll Number: TRN-2026-000376
# Date: 10-11-2026
from dataclasses import dataclass, field, asdict
import json


print("========== Product Dataclass ==========")


# Create a Product class using dataclass
@dataclass(order=True)
class Product:
    name: str
    price: float
    stock: int
    tags: list[str] = field(default_factory=list)

    # Validate product price and stock
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")

        if self.stock < 0:
            raise ValueError("Stock cannot be negative")


# Store five products in a list
products = [
    Product("Laptop", 150000, 5, ["Electronics"]),
    Product("Mouse", 1500, 0, ["Accessories"]),
    Product("Keyboard", 3000, 3, ["Accessories"]),
    Product("Monitor", 25000, 0, ["Electronics"]),
    Product("Headphones", 5000, 2, ["Audio"])
]


# Print products that are out of stock
print("Out of Stock Products:")

for product in products:
    if product.stock == 0:
        print(product.name)


print("========== Save and Load JSON ==========")


# Convert products into dictionaries
product_data = [asdict(product) for product in products]

# Save product data into a JSON file
with open("products.json", "w") as file:
    json.dump(product_data, file, indent=4)


# Load product data from the JSON file
with open("products.json", "r") as file:
    loaded_data = json.load(file)


# Convert dictionaries back into Product objects
loaded_products = [Product(**data) for data in loaded_data]


# Sort products by price
sorted_products = sorted(loaded_products, key=lambda product: product.price)

print("Products Sorted by Price:")

for product in sorted_products:
    print(f"{product.name}: Rs {product.price}")


print("========================================")
