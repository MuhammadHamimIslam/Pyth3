from urllib.request import urlopen
import json

url = urlopen("https://jsonplaceholder.typicode.com/todos/1") # open the url

data = url.read() # get the data

print(json.loads(data)) # parse the json data to dictionary