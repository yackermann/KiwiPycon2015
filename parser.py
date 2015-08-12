import urllib.request
import urllib.parse

# x = urllib.request.urlopen('https://google.com/')
# print(x.read())

# https://www.google.com/search?q=Monthy+Python

url = 'https://google.com/search'
get = {
    'q' : 'Monthy Python'
}


data = urllib.parse.urlencode(get) # Encodes to url format
data = data.encode('utf-8') # Converts to binary utf-8

# req  = urllib.request.Request(url, data) # POST
# req  = urllib.request.Request(url + '?' + data.decode("utf-8")) # GET

try:
    resp = urllib.request.urlopen(req)
    print(resp.read())

except Exception as e:
    print(str(e))