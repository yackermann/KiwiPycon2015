import re
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = 'http://store.steampowered.com/app/220'

headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36'
}

req  = urllib.request.Request(url, headers=headers) # GET

game = {}

# game = {
#     'name'        : '',
#     'price'       : 0,
#     'tags'        : [],
#     'genre'       : '',
#     'publisher'   : '',
#     'releaseDate' : '',
#     'rating'      : {
#         'count' : 0,
#         'total' : 0
#     }
# }

def cleanMe( content ):
    regex = re.compile(r'[\n|\t|\r]')
    return regex.sub('', content)

def cook( content ):
    soup = BeautifulSoup(content, 'html.parser')
    print(cleanMe(soup.find_all('div', { 'class' : "game_purchase_price price"})[0].text))

try:
    resp = urllib.request.urlopen(req)

    cook(resp.read().decode('utf-8'))
    print('Done')

except Exception as e:
    print(str(e))

