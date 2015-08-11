import urllib.request #standard library

x = urllib.request.urlopen('https://google.com/')
print(x.read())