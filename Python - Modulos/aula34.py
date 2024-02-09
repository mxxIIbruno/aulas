"""
    Comando: venv/bin/python -m http.server -d aula34_site/ 3333
"""
# requests para requisições HTTP
import requests

# http://   -> 80
# https://  -> 433

url = 'http://localhost:3333/'
response = requests.get(url=url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)
