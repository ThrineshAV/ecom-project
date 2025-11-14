import pandas as pd
import random
from faker import Faker
import os

fake = Faker()
os.makedirs("data", exist_ok=True)

# Number of rows
N_CUSTOMERS = 200
N_PRODUCTS = 100
N_ORDERS = 300
N_ORDER_ITEMS = 500
N_PAYMENTS = 300

# ---------------------------
# 1. Customers CSV
# ---------------------------
customers = []

for i in range(1, N_CUSTOMERS + 1):
    customers.append([
        i,
        fake.name(),
        fake.email(),
        random.choice(["Male", "Female", "Other"]),
        fake.date_between(start_date='-2y', end_date='today')
    ])

df_customers = pd.DataFrame(customers, columns=[
    "customer_id", "name", "email", "gender", "signup_date"
])
df_customers.to_csv("data/customers.csv", index=False)

# ---------------------------
# 2. Products CSV
# ---------------------------
products = []

categories = ["Electronics", "Fashion", "Books", "Home", "Sports"]

for i in range(1, N_PRODUCTS + 1):
    products.append([
        i,
        fake.word().title() + " Product",
        random.choice(categories),
        round(random.uniform(10, 2000), 2)
    ])

df_products = pd.DataFrame(products, columns=[
    "product_id", "product_name", "category", "price"
])
df_products.to_csv("data/products.csv", index=False)

# ---------------------------
# 3. Orders CSV
# ---------------------------
orders = []

for i in range(1, N_ORDERS + 1):
    orders.append([
        i,
        random.randint(1, N_CUSTOMERS),
        fake.date_between(start_date='-1y', end_date='today'),
        random.choice(["Completed", "Pending", "Cancelled"])
    ])

df_orders = pd.DataFrame(orders, columns=[
    "order_id", "customer_id", "order_date", "status"
])
df_orders.to_csv("data/orders.csv", index=False)

# ---------------------------
# 4. Order Items CSV
# ---------------------------
order_items = []

for i in range(1, N_ORDER_ITEMS + 1):
    order_items.append([
        i,
        random.randint(1, N_ORDERS),
        random.randint(1, N_PRODUCTS),
        random.randint(1, 5)
    ])

df_items = pd.DataFrame(order_items, columns=[
    "item_id", "order_id", "product_id", "quantity"
])
df_items.to_csv("data/order_items.csv", index=False)

# ---------------------------
# 5. Payments CSV
# ---------------------------
payments = []

methods = ["UPI", "Credit Card", "Debit Card", "Net Banking", "COD"]

for i in range(1, N_PAYMENTS + 1):
    payments.append([
        i,
        random.randint(1, N_ORDERS),
        round(random.uniform(20, 3000), 2),
        random.choice(methods),
        fake.date_between(start_date='-1y', end_date='today')
    ])

df_payments = pd.DataFrame(payments, columns=[
    "payment_id", "order_id", "amount", "payment_method", "payment_date"
])
df_payments.to_csv("data/payments.csv", index=False)

print("All 5 CSV files generated successfully inside /data folder!")

