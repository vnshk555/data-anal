import time
import random
import psycopg2
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "port": os.getenv("DB_PORT", 5432)
}

TOTAL_RECORDS = int(os.getenv("TOTAL_RECORDS"))

PRODUCTS = [
    ("iPhone 15", "Electronics", 999),
    ("Samsung TV", "Electronics", 1200),
    ("Nike Sneakers", "Fashion", 150),
    ("Adidas Hoodie", "Fashion", 80),
    ("Coffee Machine", "Home Appliances", 300),
    ("Gaming Laptop", "Electronics", 1800),
    ("Office Chair", "Furniture", 250)
]

CITIES = [
    "Moscow",
    "Saint Petersburg",
    "Kazan",
    "Novosibirsk",
    "Yekaterinburg"
]

def connect():
    while True:
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            print("Connected to DB")
            return conn
        except Exception:
            print("Waiting for DB...")
            time.sleep(5)

def generate_order():
    product = random.choice(PRODUCTS)
    quantity = random.randint(1, 5)
    price = product[2]
    total = price * quantity

    return (
        product[0],
        product[1],
        price,
        quantity,
        random.choice(CITIES),
        total
    )

def main():
    conn = connect()
    cur = conn.cursor()

    for i in range(TOTAL_RECORDS):
        order = generate_order()

        cur.execute("""
            INSERT INTO orders
            (product_name, category, price, quantity, city, total_amount)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, order)

        conn.commit()

        print(f"{i+1}/{TOTAL_RECORDS} Inserted order: {order}")
        time.sleep(1)

    print("Finished generating data.")
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()