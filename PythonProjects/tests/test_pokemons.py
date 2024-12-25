import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a9ba3235b28a5fc046418af2c04d616a'
HEADER = {'Content-Type: application/json', 'trainer_token : a9ba3235b28a5fc046418af2c04d616a'}


def test_status_code():
    reponse = requests.get(url=f'{URL}/trainers')
    assert reponse.status_code==200

def test_part_of_response():
    reponse_get = requests.get(url=f'{URL}/trainers', params={ 'trainer_id' : '13025' })
    assert reponse_get.json()["data"][0]['trainer_name'] == 'Борщик'
