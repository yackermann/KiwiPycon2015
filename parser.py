import urllib.request
import urllib.parse

# x = urllib.request.urlopen('https://google.com/')
# print(x.read())

# https://www.google.com/search?q=Monthy+Python

url = 'https://google.com/search'
get = {
    'q' : 'Monthy Python'
}

headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36'
}


data = urllib.parse.urlencode(get) # Encodes to url format
data = data.encode('utf-8') # Converts to binary utf-8

# req  = urllib.request.Request(url, data) # POST
req  = urllib.request.Request(url + '?' + data.decode("utf-8"), headers=headers) # GET

try:
    resp = urllib.request.urlopen(req)
    print(resp.read())

except Exception as e:
    print(str(e)) # 403 forbidden???
                  # Google thinks that you are a robot...
                  # ...because you do not have anything in HEADERS