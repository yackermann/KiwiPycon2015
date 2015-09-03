from bs4 import BeautifulSoup
import re

def clean( content, form ):
    expressions = {
        'tabs' : r'[\n|\t|\r]',
        'numbers' : r'[^0-9\.]'
    }
    regex = re.compile(expressions[form])
    return regex.sub('', content)

def prepare( data ):
    soup  = BeautifulSoup(data, 'html.parser')
    if not 'Site Error' in soup.find('title').text:
        game = {
            'appid'    : 0,
            'name'     : soup.find('div', {'class': 'apphub_AppName'}),
            'price'    : soup.find('div', {'class': 'game_purchase_price price'}),
            'currency' : soup.find('div', {'class': 'game_purchase_price price'}),
            'tags'     : soup.find_all('a', {'class': 'app_tag'}),
            'rating'   : {
                'count' : soup.find('meta', { 'itemprop' : 'ratingValue' }),
                'total' : soup.find('meta', { 'itemprop' : 'reviewCount' })
            }
        }
        return game

def cook( data ):
    def name( item ):
        if item != None:
            return clean(item.text, 'tabs')
        else:
            return ''

    def price( item ):
        if item != None:
            if 'Free to play' in item.text:
                return 0.0
            else:
                return clean(item.text, 'numbers')
        else:
            return 0.0

    def currency( item ):
        if item != None:
            if 'Free to play' in item.text:
                return ''
            else:
                return re.findall(r'[A-Za-z]*[$¢£¤¥֏؋৲৳৻૱௹฿៛€]', item.text)
        else:
            return ''

    def rating( item ):
        if item != None:
            return item['content']
        else:
            return 0

    game = {
        'appid'     : data['appid'],
        'name'      : name(data['name']),
        'price'     : price(data['price']),
        'currency'  : currency(data['currency']),
        'tags'      : [ clean(tag.text, 'tabs') for tag in data['tags'] ],
        'rating'    : {
            'total' : rating(data['rating']['total']),
            'count' : rating(data['rating']['count'])
        }
    }
    return game