import requests
url = "http://127.0.0.1:8080"
path = "./0926.png"
print (path)
files = {'file': open(path, 'rb')}
r = requests.post(url, files=files)
print (r.url)
print (r.text)
