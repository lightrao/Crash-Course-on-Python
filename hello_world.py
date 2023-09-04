# hello_world.py
from urllib import request

url = "https://www.baidu.com"
resp = request.urlopen(url)
print(type(resp))
