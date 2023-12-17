import mysql.connector
import csv

# connection = mysql.connector.connect(
#     host='localhost',
#     port=3307,
#     user='admin',
#     password='MyNewPass1!',
#     database='stablecoin'
# )

connection = mysql.connector.connect(
    host='database-1.c5rtl7byfjr0.us-east-1.rds.amazonaws.com',
    port=3306,
    user='admin',
    password='MyNewPass1!',
    database='stablecoin'
)

query = "SELECT * FROM stablecoin;"

cursor = connection.cursor()
cursor.execute(query)

with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write headers
    csv_writer.writerow([i[0] for i in cursor.description])
    # Write data
    csv_writer.writerows(cursor)

cursor.close()
connection.close()

