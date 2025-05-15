import requests 

payload = {"name": "pqr", "age": 34} # data to post
header = {"user-agent": "python-test"}
res = requests.post("https://httpbin.org/post", data=payload, headers=header)

print(res)
print(res.text)