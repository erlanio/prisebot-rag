import requests
import json

# Define a URL para a requisição POST
url = 'http://localhost:2024/submit_query'

# Define os headers
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Define o corpo da requisição

data = {
    'query_text': "O que é o processo PRISE?"
}

# Faz a requisição POST
response = requests.post(url, headers=headers, data=json.dumps(data))



# Exibe o conteúdo da resposta em formato JSON
try:
    response_json = response.json()
    print('Response JSON:', response_json['answer_text'])
except json.JSONDecodeError:
    print('Resposta não está em formato JSON:', response.text)