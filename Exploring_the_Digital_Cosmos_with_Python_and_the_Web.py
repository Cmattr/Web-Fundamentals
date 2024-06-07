import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['name']
            mass = mass = planet['mass']
            sideralOrbit = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit: {sideralOrbit}")

fetch_planet_data()