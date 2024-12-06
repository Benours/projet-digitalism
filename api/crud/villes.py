from fastapi import APIRouter

from api.connect import conn

router = APIRouter()

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