import requests

response = requests.get('https://serverest.dev/usuarios')
print(response.text)
