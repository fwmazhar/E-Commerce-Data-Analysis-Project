import random
import pandas as pd
from datetime import datetime, timedelta

random.seed(42)

# Configuration
num_customers = 500
num_products = 30
num_orders = 5000
duplicate_percentage = 0.05
zero_quantity_percentage = 0.05

# Categories and products
categories = [
    "Electronics",
    "Clothing",
    "Home & Kitchen",
    "Books",
    "Sports & Outdoors",
    "Beauty",
]
products = {
    "Electronics": [
        ("Wireless Earbuds", 60.25),
        ("Smartwatch", 150.50),
        ("Bluetooth Speaker", 80.75),
        ("Laptop Stand", 25.25),
        ("Portable Charger", 30.25),
    ],
    "Clothing": [
        ("Men's T-Shirt", 15.50),
        ("Women's Hoodie", 35.50),
        ("Running Shorts", 20.75),
        ("Denim Jacket", 70.75),
        ("Casual Sneakers", 55.75),
    ],
    "Home & Kitchen": [
        ("Non-stick Frying Pan", 25.25),
        ("Electric Kettle", 40.25),
        ("Vacuum Cleaner", 150.75),
        ("Set of Towels", 50.50),
        ("Air Purifier", 200.50),
    ],
    "Books": [
        ("Data Science Handbook", 45.25),
        ("Intro to Python", 30.75),
        ("Business Strategy 101", 35.50),
        ("Fiction Bestseller", 15.50),
        ("Graphic Novel", 20.25),
    ],
    "Sports & Outdoors": [
        ("Yoga Mat", 25.25),
        ("Resistance Bands", 15.75),
        ("Dumbbell Set", 75.75),
        ("Hiking Backpack", 120.50),
        ("Water Bottle", 20.25),
    ],
    "Beauty": [
        ("Face Moisturizer", 25.50),
        ("Lip Balm", 10.25),
        ("Hair Serum", 45.75),
        ("Nail Polish Set", 30.25),
        ("Facial Cleanser", 35.50),
    ],
}

# Regions
regions = [
    "USA",
    "Canada",
    "UK",
    "Germany",
    "France",
    "Australia",
    "UAE",
    "Egypt",
    "Japan",
    "Saudi Arabia",
]

# Generate customers
customers = [f"CUST{str(i).zfill(6)}" for i in range(1, num_customers + 1)]
signup_dates = [
    datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))
    for _ in range(num_customers)
]
df_customers = pd.DataFrame(
    {
        "customer_id": customers,
        "region": random.choices(regions, k=num_customers),
        "signup_date": signup_dates,
    }
)

# Generate products
product_ids = [f"PROD{str(i).zfill(6)}" for i in range(1, num_products + 1)]
product_data = []
product_idx = 0
for category, items in products.items():
    for product_name, price in items:
        product_data.append(
            {
                "product_id": product_ids[product_idx],
                "category": category,
                "product_name": product_name,
                "cost": price,
            }
        )
        product_idx += 1
df_products = pd.DataFrame(product_data)

# Generate orders
order_ids = [f"ORDER{str(i).zfill(5)}" for i in range(1, num_orders + 1)]
orders = []
zero_qty_indices = set(
    random.sample(range(num_orders), int(num_orders * zero_quantity_percentage))
)

for i, order_id in enumerate(order_ids):
    customer_id = random.choice(customers)
    product = random.choice(product_data)
    product_id = product["product_id"]
    order_date = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 364))
    quantity = 0 if i in zero_qty_indices else random.randint(1, 5)
    price = product["cost"]
    orders.append([order_id, customer_id, product_id, order_date, quantity, price])

# Add duplicate orders with new unique order_ids
num_duplicates = int(num_orders * duplicate_percentage)
duplicate_base_orders = random.choices(orders, k=num_duplicates)
start_id = num_orders + 1

for i, dup in enumerate(duplicate_base_orders, start=start_id):
    new_order_id = f"ORDER{str(i).zfill(5)}"
    new_order = [new_order_id] + dup[1:]  # Only change the order_id
    orders.append(new_order)

df_orders = pd.DataFrame(
    orders,
    columns=[
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "price",
    ],
)

# Save to CSV
df_customers.to_csv("customers.csv", index=False)
df_products.to_csv("products.csv", index=False)
df_orders.to_csv("orders.csv", index=False)

print("✅ customers.csv, products.csv, and orders.csv have been generated.")
