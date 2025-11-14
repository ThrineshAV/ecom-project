import sqlite3
import pandas as pd
import os

DATA_DIR = "data"
DB_NAME = "ecommerce.db"

def create_connection(db_name):
    return sqlite3.connect(db_name)

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            gender TEXT,
            signup_date TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            category TEXT,
            price REAL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            order_date TEXT,
            status TEXT,
            FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            item_id INTEGER PRIMARY KEY,
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY(order_id) REFERENCES orders(order_id),
            FOREIGN KEY(product_id) REFERENCES products(product_id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY,
            order_id INTEGER,
            amount REAL,
            payment_method TEXT,
            payment_date TEXT,
            FOREIGN KEY(order_id) REFERENCES orders(order_id)
        );
    """)

    conn.commit()


def load_csv(conn, filename, table):
    df = pd.read_csv(os.path.join(DATA_DIR, filename))
    df.to_sql(table, conn, if_exists="append", index=False)
    print(f"Loaded → {table}")


def main():
    conn = create_connection(DB_NAME)
    create_tables(conn)

    load_csv(conn, "customers.csv", "customers")
    load_csv(conn, "products.csv", "products")
    load_csv(conn, "orders.csv", "orders")
    load_csv(conn, "order_items.csv", "order_items")
    load_csv(conn, "payments.csv", "payments")

    conn.close()
    print("\nAll data loaded into ecommerce.db successfully!")


if __name__ == "__main__":
    main()
