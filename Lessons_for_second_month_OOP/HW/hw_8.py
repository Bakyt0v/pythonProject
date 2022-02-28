
import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except ConnectionError as e:
        print(e)
    return conn


def create_table(conn, product):
    try:
        c = conn.cursor()
        c.execute(product)
    except ConnectionError as e:
        print(e)

db = r'hw.db'
conn = create_connection(db)
sql_create_product_table = '''
CREATE TABLE product (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0
)
'''
if conn is not None:
    print('Successfully connected')
    create_table(conn, sql_create_product_table)
    conn.close()