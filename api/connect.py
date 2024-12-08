import mysql.connector

# Avec Docker

# Connect to database

conn = mysql.connector.connect(
    host="172.17.0.2",
    user="root",
    password="root",
    port="3306",
    database="data_france"
)

# En local

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     port="3307",
#     database="data_france"
# )