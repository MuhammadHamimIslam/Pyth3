from urllib.request import Request, urlopen
import urllib.error as error 

import json

url = urlopen("https://jsonplaceholder.typicode.com/todos/1") # open the url

data = url.read() # get the data

print(json.loads(data)) # parse the json data to dictionary

"Request object"
# request object follows Request(url, data, header, originRequestHost, method)

dataUrl = Request("https://muhammadhamimislam.github.io/country_info/info.json")
response = urlopen(dataUrl) # returns http request object 
responseData = response.read() # read the response data
print(json.loads(responseData)) # show as python dictionary 

"Some errors are defined in urllib.error library"

# Url Error 
try:
    urlObj = "https://www.invalidurl.com"
    urlopen(urlObj)
except error.URLError as e:
    print(e)
    
# HTTP Error 
try:
    url = "https://muhammadhamimislam.github.io/country_info/index.htm"
    data = urlopen(url)
    print(data.read())
except error.HTTPError as e:
    print(e)
    print(e.code) # returns the request code