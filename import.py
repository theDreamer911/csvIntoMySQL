import MySQLdb
import csv
import sys
conn = MySQLdb.connect(host="127.0.0.1", user="root", password="", database="Fruit_Shop")

cursor = conn.cursor()
csv_data = csv.reader(open('products.csv'))
header = next(csv_data)

print('Importing the CSV Files')
for row in csv_data:
    print(row)
    cursor.execute(
        "INSERT INTO product (id,name,price,stock) VALUES (%s, %s, %s, %s)", row)

conn.commit()
cursor.close()
print('Done')
