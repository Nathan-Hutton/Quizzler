import requests

COMPUTER_CATEGORY = 18

parameter = {
    'amount': 10,
    'type': 'boolean',
}

response = requests.get('https://opentdb.com/api.php?', params=parameter)
response.raise_for_status()
question_data = response.json()['results']
