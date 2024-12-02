from bs4 import BeautifulSoup
import requests

# Ambil halaman web
url = 'https://www.speedssh.com'
response = requests.get(url)

print(response.text)
