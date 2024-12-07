from fastapi import APIRouter

from api.connect import conn

router = APIRouter()

# Methodes CREATE

# Créer une nouvelle ville
@router.post("/create_city")
def create_city(commune: str, code_postal: str, departement: str):
    cursor = conn.cursor()
    createCity = """INSERT INTO villes(
        commune,
        code_postal,
        departement)
        VALUES (%s,%s,%s)"""
    cursor.execute(createCity, (commune.upper(), code_postal, departement))
    conn.commit()
    return "Successful create : [%s, %s, %s]" % (commune, code_postal, departement)

# Methodes GET

# Récupérer toutes les villes d'un département
@router.get('/get_cities_by_dep')
def get_cities_by_dep(departement: str):
    cursor = conn.cursor()
    getCitiesByDep = """SELECT * FROM villes WHERE departement=%s""" % (departement)
    cursor.execute(getCitiesByDep)
    city = cursor.fetchall()
    return city

# Récupérer les infos d'une ville par son nom
@router.get('/get_city_by_name')
def get_city_by_name(commune: str):
    cursor = conn.cursor()
    getCityByName = """SELECT * FROM villes WHERE commune=%s""" % (commune)
    cursor.execute(getCityByName)
    city = cursor.fetchall()
    return city

# Methodes UPDATE

# Mettre à jour une ville
@router.put("/update_city")
def update_city(old_commune: str, old_code_postal: str, commune: str, code_postal: str, departement: str):
    cursor = conn.cursor()
    updateCity = """UPDATE villes 
        SET commune=%s, 
        code_postal=%s, 
        departement=%s 
        WHERE commune=%s and code_postal=%s"""
    cursor.execute(updateCity, (commune.upper(), code_postal, departement, old_commune.upper(), old_code_postal))
    conn.commit()
    return "Successful update : [%s, %s, %s]" % (commune, code_postal, departement)