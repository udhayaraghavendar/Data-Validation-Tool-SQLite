import sqlite3


conn = sqlite3.connect("sample_data.db")

cursor = conn.cursor()

# cursor.execute("create table customers(customer_id int primary key, name text)")

# cursor.execute("create table orders(order_id INT PRIMARY KEY,customer_id INT, order_date TEXT,delivery_date TEXT,amount REAL)")

# data = [(1, 'Arun Kumar'),
#          (2, 'Karthikeyan'),
#          (3, 'Priya Dharshini'),
#          (4, 'Suresh Babu'),
#          (5, 'Meena Lakshmi')]
#
# cursor.executemany("insert into customers values (?,?)",data)
# conn.commit()

data1 = [

# -- 1 VALID
(301, 1, '2025-01-10', '2025-01-12', 250.00),

# -- 2 VALID
(302, 2, '2025-01-11', '2025-01-13', 499.00),

# -- 3 INVALID: customer_id NULL
(303, "NULL", '2025-01-12', '2025-01-14', 320.00),

# -- 4 INVALID: order_date NULL
(304, 3, "NULL", '2025-01-15', 150.00),

# -- 5 INVALID: timestamp mismatch (order_date > delivery_date)
(305, 1, '2025-01-20', '2025-01-19', 400.00),

# -- 6 INVALID: invalid relationship (customer 999 not in customers table)
(306, 999, '2025-01-18', '2025-01-20', 275.00),

# -- 7 VALID
(307, 4, '2025-01-14', '2025-01-16', 510.00),

# -- 8 VALID
(308, 5, '2025-01-16', '2025-01-18', 620.00),

# -- 9 INVALID: duplicate order_id (308 repeated)
(308, 2, '2025-01-17', '2025-01-19', 700.00),

# -- 10 VALID
(309, 3, '2025-01-19', '2025-01-21', 350.00)]


# cursor.executemany( "insert into orders values (?,?,?,?,?) ", data1)
cursor.execute("update orders set order_date = ? where order_id =? ",(None,304))
conn.commit()
# cursor.execute("create table orders(order_id INT, customer_id INT, order_date TEXT, delivery_date TEXT, amount REAL) ")

# check orders col
# cursor.execute("pragma table_info(orders)")
# result = cursor.fetchall()
#
# for row in result :
#     print(row[1], row[2])


# check orders content

cursor.execute("select * from orders")
result = cursor.fetchall()
for row in result :
    print(row)
conn.close()
