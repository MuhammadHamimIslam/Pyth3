"To work with url, Python has a package nameed urllib which have some modules urllib.parse, urllib.request, urllib.error, urllib.robotparser"

from urllib.parse import urlparse, parse_qs, urlunparse

url = "http://color-pulse.pages.dev/home?darkmode=True"

parsedUrl = urlparse(url)

print("type is: ", type(parsedUrl))
print("Scheme: ", parsedUrl.scheme) # returns the scheme of the url
print("netloc: ", parsedUrl.netloc) # returns the netloc
print("path: ", parsedUrl.path) # returns the path
print("params: ", parsedUrl.params) # returns the params
print("query string: ", parsedUrl.query) # returns the query string of the url
print("fragment: ", parsedUrl.fragment) # returns the fragment
print("query dict: ", parse_qs(parsedUrl.query)) # dictionary form of query string

urlList = ["http", "color-pulse.pages.dev", "/home", "", "darkmode=True", ""] # url list

unParsedUrl = urlunparse(urlList) # unparse the url
print(unParsedUrl)