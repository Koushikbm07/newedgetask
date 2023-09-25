
from flask import Flask, render_template, request, redirect
import sqlite3
import random
import math

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()

    # products_per_page=20;
    # page=request.args.get('page')
    # last=math.ceil(len(products)/products_per_page)
    
    # if(not str(page).isnumeric()):
    #     page=1
    # page=int(page)

    # if(page!=last):
    #     products_list=products[(page-1)*products_per_page:((page-1)*products_per_page + products_per_page )]
    # else:
    #     products_list=products[(page-1)*products_per_page : ((page-1)*products_per_page + products_per_page ) -10]

    # if(page==1):
    #     prev='#'
    #     next="/?page="+str(page+1)
    # elif(page==last):
    #     next="#"
    #     prev="/?page="+str(page-1)
    # else:
    #     prev="/?page="+str(page-1)
    #     next="/?page="+str(page+1)
        
    
    return render_template('index.html',products_list=products)


@app.route('/generate_products')
def generate_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products')  # Clear existing data
    products = []

    for i in range(1, 51):
        product_name = f'Item {i}'
        stock_on_hand = random.randint(0, 50)
        cursor.execute('INSERT INTO products (Product_Name, Stock_On_Hand) VALUES (?, ?)', (product_name, stock_on_hand))
        products.append((product_name, stock_on_hand))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/sort_asc')
def sort_asc():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products ORDER BY id ASC ')
    products = cursor.fetchall()
    conn.close()

    # return redirect('/')
    return render_template('index.html',products_list=products)


@app.route('/sort_desc')
def sort_desc():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products ORDER BY Stock_On_Hand DESC')
    products = cursor.fetchall()
    conn.close()
   
    return render_template('index.html',products_list=products)
    # return redirect('/')
    
@app.route('/reduce_stock')
def reduce_stock():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET Stock_On_Hand = Stock_On_Hand - 2 WHERE Stock_On_Hand>1')
    conn.commit()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()

    # return redirect('/')
    return render_template('index.html',products_list=products)

@app.route('/increase_stock')
def increase_stock():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET Stock_On_Hand = Stock_On_Hand + 2 WHERE id % 2 = 0')
    conn.commit()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    # return redirect('/')
    return render_template('index.html',products_list=products)
    



# if __name__ == '__main__':
#     app.run(debug=False,host='0.0.0.0')
