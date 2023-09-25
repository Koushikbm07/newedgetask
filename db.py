import sqlite3


conn = sqlite3.connect('products.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE  IF EXISTS products')
cursor.execute(''' 
               CREATE TABLE  products(
                    id INTEGER PRIMARY KEY,
                    Product_Name  TEXT  NOT NULL,
                    Stock_On_Hand  INTEGER NOT NULL 
                )''')

conn.commit()
conn.close()