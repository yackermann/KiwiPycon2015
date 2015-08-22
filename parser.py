import re, json
from bs4 import BeautifulSoup

# http://store.steampowered.com/app/220/ # Price
# http://store.steampowered.com/app/7340 # No price
# http://store.steampowered.com/app/6370 # Free to play

def clean( content, form ):
    expressions = {
        'tabs' : r'[\n|\t|\r]',
        'numbers' : r'[^0-9\.]'
    }
    regex = re.compile(expressions[form])
    return regex.sub('', content)
# List access exceptioner 
def lax(l, index):
    try:
        return l[index]
    except: 
        return None
def toInt( num ):
    try:
        return int(num)
    except:
        try:
            return float(num)
        except:
            print(num)
            return 0

def cook( data ):
    def name( d ):
        if d != None:
            return clean(d.text, 'tabs')

    def price( d ):
        if d != None:
            d = d.text

            if 'Free to Play' in d:
                return 0
            elif d == '':
                return 0
                
            return toInt(clean(d, 'numbers'))
        return 0

    def currency( d ):
        if d != None:
            d = d.text
            if 'Free to Play' in d:
                return ''
            elif d == '':
                return ''
                
            return lax(re.findall(r'[A-Za-z]*[$¢£¤¥֏؋৲৳৻૱௹฿៛€]', d), 0)
        return ''

    def rating( d ):
        for var in d:
            if d[var] != None:
                d[var] = int(d[var]['content'])
            else:
                d[var] = 0
        return d

    return {
        'name'     : name(data['name']),
        'price'    : price(data['price']),
        'currency' : currency(data['price']),
        'tags'     : data['tags'],
        'rating'   : rating(data['rating'])
    }


def prepare( content ):
    soup = BeautifulSoup(content, 'html.parser')
    title = soup.find('title').text
    if title != 'Site Error':
        game = {}
        # def sortMixedVariable():
        #     mixed = soup.find_all('div', { 'class' : 'details_block' })[0].text.replace('\n\n', '\n').replace(':\n', ':').split('\n')
        #     toArray = [ item.split(':') for item in mixed if item != '' ]
        #     metaInfo = {}
        #     for item in toArray:
        #         metaInfo[ item[0].replace(' ', '').lower() ] = item[1]
        #     return metaInfo

        # mixed = ''

        # try:
        #     mixed = sortMixedVariable()
        # except:
        #     mixed = {
        #         'genre'       : '',
        #         'publisher'   : '',
        #         'releasedate' : ''
        #     }

        # print(mixed)
        try:
            game = {
                'name'        : lax(soup.find_all('div', { 'class' : 'apphub_AppName' }), 0),
                'price'       : lax(soup.find_all('div', { 'class' : 'game_purchase_price price' }), 0),
                'tags'        : [ clean(tag.text, 'tabs') for tag in soup.find_all('a', {'class' : 'app_tag'}) ],
                # 'genre'       : mixed['genre'],
                # 'publisher'   : mixed['publisher'],
                # 'releasedate' : mixed['releasedate'],
                'rating'      : {
                    'count' : lax(soup.find_all(attrs={ 'itemprop' : 'reviewCount'}), 0),
                    'total' : lax(soup.find_all(attrs={ 'itemprop' : 'ratingValue'}), 0)
                }
            }
        except Exception as e:
            print(json.dumps({
                'Error': str(e)
            }, indent=4, separators=(',', ': ')))

        export = cook(game)

        return {'ok': True, 'data' : export}
    else:
        return {'ok': False}