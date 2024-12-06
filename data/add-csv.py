import csv
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port="3307",
    database="data_france"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE data_france")

# mycursor.execute("CREATE TABLE villes (commune VARCHAR(255), code_postal VARCHAR(255), departement VARCHAR(255))")

with open('data/20230823-communes-departement-region.csv', newline='') as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        code_commune_INSEE, nom_commune_postal, code_postal, libelle_acheminement, ligne_5, latitude, longitude, code_commune, article, nom_commune, nom_commune_complet, code_departement, nom_departement, code_region, nom_region = row
        nom_commune_complet_maj = nom_commune_complet.upper()
        
        if len(code_postal) == 4:
            departement = '0' + str(code_postal)[0:1]
        elif len(code_postal) == 5 and int(str(code_postal)[0:2]) < 96:
            departement = str(code_postal)[0:2]
        elif int(str(code_postal)[0:2]) == 97:
            departement = str(code_postal)[0:3]
        else:
            departement = "N/A"

        sql = "INSERT INTO villes (commune, code_postal, departement) VALUES (%s, %s, %s)"
        val = (nom_commune_complet_maj, code_postal, departement)
        mycursor.execute(sql, val)

mydb.commit()
    
