import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # Adresse de l'hôte, souvent 'localhost' ou '127.0.0.1'
    user="root",  # Utilisateur MySQL
    password="root",  # Mot de passe
    port="3307",
    database="data_france"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE data_france")

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)

# mycursor.execute("CREATE TABLE villes (commune VARCHAR(255), code_postal VARCHAR(255), departement VARCHAR(255))")

# mycursor.execute("DROP TABLE villes")

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)

# mycursor.execute("SELECT * FROM villes")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
