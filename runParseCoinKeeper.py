import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://coinkeeper.me/introduce-yourself'
page = requests.get(url)
soup = BeautifulSoup(page, "html5lib")
i = soup.find('body > input', {'id':'recaptcha-token'}) # the input tag looks like that: <input type="hidden" id="recaptcha-token" value="03AGdBq27IFqX2_...">

# print(soup)
print(i)
