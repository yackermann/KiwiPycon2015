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

        with urllib.request.urlopen(req, timeout=2) as response:
            return {
                'ok'  : True,
                'url' : response.url,
                'data': response.read().decode('utf-8')
            }
    except Exception as e:
        return {'ok' : False, 'error': e }

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

        while True:
            data = get(url)
            if(data['ok']):
                if data['url'] == url:
                    item = cook(data['data'])
                    if item['ok']:
                        print('Parsing:', url)
                        items.push(item)
                    else:
                        print('Skipping:', url)
                else:
                    print('Skipping:', url)
            
                break
            else:
                print('Redoing:', url)

            sleep(0.33)

    return items


def StartClient():
    print('Starting client...')
    while True:
        task = get(mothership['get'])
        if task['ok']:
            todo = json.loads(task['data'])
            r = range(todo['start'], todo['stop'], todo['step'])
            data = bruteforceRange(r)
            post(mothership['post'], json.dumps(data))
        else:
            print('Failed', task)
        sleep(0.5)


# url = 'http://store.steampowered.com/app/220'