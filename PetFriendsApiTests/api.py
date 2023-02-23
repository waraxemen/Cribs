import requests
import json
from settings import key

import requests_toolbelt  # для передачи файлов, _ вместо - т.к. - принимает как команду
from requests_toolbelt.multipart.encoder import MultipartEncoder  # Из неё импортируем класс MultipartEncoder

created_pets = ['']

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email: str, password: str) -> json:
        header = {'email': email, "password": password}
        response = requests.get(self.base_url+'api/key', headers=header)
        status = response.status_code
        result = ''
        try:
            result = response.json()
        except:
            result = response.text
        return status, result
    def get_list_of_pets(self,auth_key, filter):
        header = {'auth_key': auth_key['key']}  # указываем чтобы из auth_key взял значение 'key'  {'key': '0000000000'}
        filter = {'filter': filter}
        response = requests.get(self.base_url+'api/pets', headers=header, params=filter)
        status = response.status_code
        print(auth_key)
        result = ''
        try:
            result = response.json()
        except:
            result = response.text
        return status, result

    def post_add_new_pet_with_photo(self, auth_key: str, name: str, animal_type: str, age: str , pet_photo: str):
        data = MultipartEncoder(  # для добавления фото
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), "images/Pushistick.jpg")})
        header = {'auth_key': key, 'Content-Type': data.content_type}
        response = requests.post(self.base_url + 'api/pets', headers=header, data=data)  # data содержит 4 нужных ключа
        status = response.status_code
        try:
            result = response.json()
        except:
            result = response.text
        return status, result

    def delete_new_pet(self, auth_key, pet_id):
        header = {'auth_key': auth_key['key']}
        pet_id = {'pet_id': pet_id}
        response = requests.delete(self.base_url + f'api/pets/{pet_id}', headers=header)
        status = response.status_code
        try:
            result = response.json()
        except:
            result = response.text
        return status, result

