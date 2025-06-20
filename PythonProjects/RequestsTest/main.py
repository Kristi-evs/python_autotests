import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'dd8b1e5f8e72c939150728089e9115d3'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_regisration = {
    "trainer_token": TOKEN,
    "email": "kristinochka.rudkovskaya@mail.ru",
    "password": "Kk9887453556"
}
body_confirmation = {
    "trainer_token": TOKEN
    }
body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}


'''responce = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_regisration)
print(responce.text)'''

'''responce_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(responce_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

id = response_create.json()['id']
print(id)

body_create = {
   "pokemon_id" : id,
    "name": "kris",
    "photo_id": 2
}

response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

{
    "pokemon_id" : id
}

response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_create)
print(response_create.text)