import requests

#response = requests.get("https://muhammadhamimislam.github.io/country_info/info.json")
response = requests.get("https://restcountries.com/v3.1/all")

print(response)

print(response.ok)

print(response.status_code)

print(response.text)

print(response.content)