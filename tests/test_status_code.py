import requests

get_response = requests.get(url='https://the-internet.herokuapp.com/status_codes/200')
print(get_response.status_code)
assert get_response.status_code == 200

get_response = requests.get(url='https://the-internet.herokuapp.com/status_codes/301')
print(get_response.status_code)
assert get_response.status_code == 301

get_response = requests.get(url='https://the-internet.herokuapp.com/status_codes/404')
print(get_response.status_code)
assert get_response.status_code == 404

get_response = requests.get(url='https://the-internet.herokuapp.com/status_codes/500')
print(get_response.status_code)
assert get_response.status_code == 500
