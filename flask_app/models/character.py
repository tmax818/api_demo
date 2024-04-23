import requests
from pprint import pprint

BASE_URL = "https://rickandmortyapi.com/api/character"

class Character:

    def __init__(self, data) -> None:
        self.name = data['name']
        self.image = data['image']
        self.location = data['location']
        self.type = data['type']
        self.location_name = data['location']['name']


    @staticmethod
    def get_data():
        data = requests.get(BASE_URL).json()
        characters = []
        pprint(data['results'])
        for character in data['results']:
            characters.append(Character(character))
     
        return characters


