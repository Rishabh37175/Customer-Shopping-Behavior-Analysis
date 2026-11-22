import pandas as pd
import mysql.connector
from getpass import getpass

# Load cleaned CSV
df = pd.read_csv("data/customer_shopping_behavior_cleaned.csv")

print("CSV loaded successfully!")
print("Total records:", len(df))

# Ask for MySQL password
password = getpass("Enter MySQL root password: ")

try:
    # Connect to MySQL
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="customer_behavior"
    )

    cursor = connection.cursor()

    # Check whether the table already contains records
    cursor.execute("SELECT COUNT(*) FROM customer_shopping_behavior")
    existing_count = cursor.fetchone()[0]

    if existing_count > 0:
        print("Table already contains records. Import skipped.")

    else:
        # SQL query to insert records
        insert_query = """
        INSERT INTO customer_shopping_behavior (
            customer_id, age, gender, item_purchased, category,
            purchase_amount_usd, location, size, color, season,
            review_rating, subscription_status, shipping_type,
            discount_applied, previous_purchases, payment_method,
            frequency_of_purchases
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Convert DataFrame rows into Python tuples
        records = [
            tuple(
                value.item() if hasattr(value, "item") else value
                for value in row
            )
            for row in df.itertuples(index=False, name=None)
        ]

        # Insert records into MySQL
        cursor.executemany(insert_query, records)

        connection.commit()

        print("Data imported successfully!")
        print("Records inserted:", cursor.rowcount)

    cursor.close()
    connection.close()

except mysql.connector.Error as error:
    print("MySQL Error:", error)