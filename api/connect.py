import mysql.connector

# Connect to database
conn = mysql.connector.connect(
    host="172.17.0.2",
    user="root",
    password="root",
    port="3306",
    database="data_france"
)
