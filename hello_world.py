from urllib import request

url = "https://www.google.com"
resp = request.urlopen(url)
print(type(resp))
