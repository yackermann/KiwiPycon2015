import re, json
from bs4 import BeautifulSoup

def clean( content, form ):
    expressions = {
        'tabs' : r'[\n|\t|\r]',
        'numbers' : r'[^0-9\.]'
    }
    regex = re.compile(expressions[form])
    return regex.sub('', content)

def cook( content ):
    soup = BeautifulSoup(content, 'html.parser')
    title = soup.find('title').text
    if title != 'Site Error':
        def sortMixedVariable():
            mixed = soup.find_all('div', { 'class' : 'details_block' })[0].text.replace('\n\n', '\n').replace(':\n', ':').split('\n')
            toArray = [ item.split(':') for item in mixed if item != '' ]
            metaInfo = {}
            for item in toArray:
                metaInfo[ item[0].replace(' ', '').lower() ] = item[1]
            return metaInfo

        mixed = sortMixedVariable()

        game = {
            'name'        : clean(soup.find_all('div', { 'class' : 'apphub_AppName' })[0].text, 'tabs'),
            'price'       : float(clean(soup.find_all('div', { 'class' : "game_purchase_price price"})[0].text, 'numbers')),
            'tags'        : [ clean(tag.text, 'tabs') for tag in soup.find_all('a', {'class' : 'app_tag'}) ],
            'genre'       : mixed['genre'],
            'publisher'   : mixed['publisher'],
            'releasedate' : mixed['releasedate'],
            'rating'      : {
                'count' : float(clean(soup.find_all(attrs={ 'itemprop' : 'reviewCount'})[0]['content'], 'numbers')),
                'total' : int(clean(soup.find_all(attrs={ 'itemprop' : 'ratingValue'})[0]['content'], 'numbers'))
            }
        }

        return {'ok': False, 'data' : game}
    else:
        return {'ok': False}