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

# mycursor.execute("ALTER DATABASE data_france CHARACTER SET utf8 COLLATE utf8_general_ci")

# mycursor.execute("""CREATE TABLE villes (
#                  commune VARCHAR(255) NOT NULL, 
#                  code_postal VARCHAR(5) NOT NULL, 
#                  departement VARCHAR(3) NOT NULL,
#                  CONSTRAINT PK_villes PRIMARY KEY (commune,code_postal)
#                  )""")

villes_de_france = set()

with open('data/20230823-communes-departement-region.csv', newline='', encoding='utf-8') as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:

        # Extraction des données du csv
        code_commune_INSEE, nom_commune_postal, code_postal, libelle_acheminement, ligne_5, latitude, longitude, code_commune, article, nom_commune, nom_commune_complet, code_departement, nom_departement, code_region, nom_region = row
        
        # Modification de la donnée
        nom_commune_complet_maj = nom_commune_complet.upper()
        
        if len(code_postal) == 4:
            departement = '0' + str(code_postal)[0:1]
        elif len(code_postal) == 5 and (code_postal[0:2] in ["2A", "2B"] or str(code_postal)[0:2] == "2B" or int(str(code_postal)[0:2]) < 96):
            departement = str(code_postal)[0:2]
        elif int(str(code_postal)[0:2]) == 97:
            departement = str(code_postal)[0:3]
        else:
            departement = "N/A"
        
        # Chargement de la donnée dans un Set 
        villes_de_france.add((nom_commune_complet_maj, code_postal, departement))

# Insertion des données dans la base de données
sql = "INSERT INTO villes (commune, code_postal, departement) VALUES (%s, %s, %s)"

for ville in villes_de_france:
    try:
        mycursor.execute(sql, ville)  # Exécuter la requête pour chaque ville

    except mysql.connector.Error as err:
        print("Erreur : %s " % (err))  # Gestion des erreurs SQL

# Commit des changements
mydb.commit()

# Fermeture de la connexion
mycursor.close()
mydb.close()

print("Données insérées avec succès !")
    
