import requests

def get_pokemon_details(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()

    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    weight = data['weight']

    print(f"\nName: {name}")
    print("Abilities:")
    for ability in abilities:
        print(f"- {ability}")
    print(f"weight: {weight}")

get_pokemon_details('pikachu')
get_pokemon_details('charmander')
get_pokemon_details('eevee')