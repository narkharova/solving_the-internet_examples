import requests

first_body = \
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


second_body = \
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


def test_post_request():
    # Создаём и отправляем данные для запроса
    post_request = requests.post('https://petstore.swagger.io/v2/pet', json=first_body)
    assert post_request.status_code == 200


def test_get_response():
    # Получаем данные
    get_response = requests.get(url='https://petstore.swagger.io/v2/pet/100')
    assert get_response.status_code == 200


def test_del_response():
    # Удаляем данные
    del_response = requests.delete(url='https://petstore.swagger.io/v2/pet/100')
    assert del_response.status_code == 200


def test_jsoned():
    # Создали данные
    put_request = requests.put('https://petstore.swagger.io/v2/pet', json=second_body)
    jsoned = put_request.json()
    assert jsoned['name'] == 'nani'