from config import dbname, user, password, host
import psycopg2
from psycopg2 import Error


def create_table():
    """Create tables"""
    db_tables = (
        """
        CREATE TABLE customer (
            customer_id SERIAL PRIMARY KEY,
            customer_name VARCHAR(255) NOT NULL,
            customer_phone VARCHAR(15) NOT NULL,
            customer_email VARCHAR(255) NOT NULL
            )
        """,
        """
        CREATE TABLE cart (
        cart_id SERIAL PRIMARY KEY,
        cart_customer_id INTEGER REFERENCES customer(customer_id)
        )
        """,
        """
        CREATE TABLE product (
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(255) NOT NULL,
            product_description TEXT, 
            product_price INTEGER
        )
        """,
        """
        CREATE TABLE cart_prod (
        cart_prod_id INTEGER REFERENCES cart(cart_id),
        cart_prod_product_id INTEGER REFERENCES product(product_id)
        )
        """,
        """
        CREATE TABLE product_photo (
        product_photo_id SERIAL PRIMARY KEY,
        product_photo_url VARCHAR(255) NOT NULL,
        product_id INTEGER REFERENCES product (product_id)
        )    
        """
    )
    conn = None

    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        cursor = conn.cursor()
        for db_table in db_tables:
            cursor.execute(db_table)
            cursor.close()
    except (Exception, Error) as error:
        print('An error occurred while working with the database', error)
    finally:
        conn.commit()
        conn.close()
        print('Database connection closed')


if __name__ == '__main__':
    create_table()
