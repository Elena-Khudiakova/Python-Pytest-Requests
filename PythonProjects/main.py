import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a9ba3235b28a5fc046418af2c04d616a'
HEADER = {'Content-Type: application/json', 'trainer_token : a9ba3235b28a5fc046418af2c04d616a'}
body_registration= {
    "trainer_token": TOKEN,
    "email": "khudiakova-lena.91@yandex.ru",
    "password": "Zaxar1002"
}

bode_create={
    "name": "Бульбазавр",
    "photo_id": 1
}

bode_put_name_Pokemon= {
    "pokemon_id": "POKEMON_id" ,
    "name": "New Name",
    "photo_id": 2
}

bode_pokeball= {
    "pokemon_id": "POKEMON_id"
}

response=requests.post(url=f'{URL}trainers/reg', headers=HEADER,json=body_registration)
print(response.text)

response_create=requests.post(url=f'{URL}/pokemons',headers=HEADER,json=bode_create)
print(response_create.text)

POKEMON_id=response_create.json()[id]

response_put_name_Pokemon=requests.put(url=f'{URL}/pokemons',headers=HEADER,json=bode_put_name_Pokemon)
print(response_put_name_Pokemon.text)

response_pokeball=requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER,json=bode_pokeball)
