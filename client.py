import urllib.request, urllib.parse, json
from parser import *
from time import sleep

mothership = {
    'get' : 'http://localhost:8888/get',
    'post' : 'http://localhost:8888/post'
}

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36'}

def get(url):
    try:
        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req) as response:
            return {
                'ok' : True,
                'url': response.url,
                'data': response.read().decode('utf-8')
            }
    except:
        return {'ok' : False }

def post(url, values):
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data, headers=headers)

    with urllib.request.urlopen(req) as response:
        return {
            'url': response.url,
            'data': response.read().decode('utf-8')
        }

def bruteforceRange(r):
    items = []
    for id in r:
        url = url = 'http://store.steampowered.com/app/' + str(id)
        data = get(url)
        if data['url'] == url:
            item = cook(data['data'])
            if item['ok']:
                print('Parsing:', url)
                items.push(item)
            else:
                print('Skipping:', url)

        else:
            print('Skipping:', url)
        sleep(0.33)

    return items


def StartClient():
    print('Starting client...')
    while True:
        task = json.loads(get(mothership['get'])['data'])
        r = range(task['start'], task['stop'], task['step'])
        data = bruteforceRange(r)
        post(mothership['post'], json.dumps(data))


# url = 'http://store.steampowered.com/app/220'