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

        try:
            game = {
                'name'        : soup.find('div', { 'class' : 'apphub_AppName' }),
                'price'       : soup.find('div', { 'class' : 'game_purchase_price price' }),
                'tags'        : [ clean(tag.text, 'tabs') for tag in soup.find_all('a', {'class' : 'app_tag'}) ],
                'rating'      : {
                    'count' : soup.find(attrs={ 'itemprop' : 'reviewCount'}),
                    'total' : soup.find(attrs={ 'itemprop' : 'ratingValue'})
                }
            }
        except Exception as e:
            print(json.dumps({
                'Error': str(e)
            }, indent=4, separators=(',', ': ')))

            return {'ok': False}

        export = cook(game)

        return {'ok': True, 'data' : export}
    else:
        return {'ok': False}