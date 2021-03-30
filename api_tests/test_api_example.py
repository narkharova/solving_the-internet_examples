import requests

# Создаём и отправляем данные для запроса
body = \
    {
        "id": 100,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

post_request = requests.post('https://petstore.swagger.io/v2/pet', json=body)

# Получаем данные
get_response = requests.get(url='https://petstore.swagger.io/v2/pet/100')
assert get_response.status_code == 200

# Улаляем данные
deL_response = requests.delete(url='https://petstore.swagger.io/v2/pet/100')
assert deL_response.status_code == 200

# Создали данные
body = \
    {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "nani",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

put_request = requests.put('https://petstore.swagger.io/v2/pet', json=body)
jsoned = put_request.json()
assert jsoned['name'] == 'nani'