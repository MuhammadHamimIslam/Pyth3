import requests

# setting header
headers = {"user-agent": "python-project"}
response = requests.get("https://muhammadhamimislam.github.io/country_info/info.json", headers= headers)

print(response)

print(response.ok) # checks if response is ok

print(response.status_code) # returns tje response status code -> 200 is normal 

print(response.text) # get the response text

print(response.content) # get the content in binary format

print(response.encoding) # returns the encoding system 

print(response.json()) # returns the response as dictionary parsing the json

print(response.headers) # returns the response headers


payload = {"q": "python"}

r = requests.get("https://www.bing.com/search", params=payload) # adding additional parameters to the response object 
print(r.url) # returns the url adding the parameters 

