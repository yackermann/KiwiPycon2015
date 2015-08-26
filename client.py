import urllib.request, urllib.parse, json
from parser import *
from time import sleep

mothership = {
    'get' : 'http://192.241.194.12:8888/get',
    'post' : 'http://192.241.194.12:8888/post'
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
    try:
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')

        req = urllib.request.Request(url, data, headers=headers)

        with urllib.request.urlopen(req) as response:
            return {
                'url': response.url,
                'data': response.read().decode('utf-8')
            }
    except Exception as e:
        return {'ok' : False, 'error': e }

def bruteforceRange(r):
    games = []

    for id in r:
        url = url = 'http://store.steampowered.com/app/' + str(id)
        tries = 0
        while True:
            # 3 tries
            tries = tries + 1
            if tries > 3:
                print('Failed:', 3)
                break

            data = get(url)
            if(data['ok']):
                if data['url'] == url:
                    item = prepare(data['data'])
                    if item['ok']:
                        print('Parsing:', url)
                        item['data']['appid'] = id
                        games.append(item['data'])
                    else:
                        print('Skipping:', url)
                else:
                    print('Skipping:', url)
            
                break
            else:
                print('Redoing:', url)

            sleep(0.05)

    return games


def StartClient():
    print('Starting client...')
    while True:
        task = ''
        try:
            task = get(mothership['get'])
        except:
            print('Server is down')
            sleep(1)
            continue

        if task['ok']:
            todo = json.loads(task['data'])
            if 'start' in todo and 'stop' in todo and 'step' in todo:
                print('Received task:', todo['start'], 'to', todo['stop'], 'step', todo['step'] )
                r = range(todo['start'], todo['stop'], todo['step'])
                # r = range(7300, 7500, 10)
                data = bruteforceRange(r)
                post(mothership['post'], {'method': 'data', 'data' : json.dumps(data)})
            else:
                print('Not task')
                sleep(1)
        else:
            print('Failed to receive task')
        sleep(1)

StartClient()
# url = 'http://store.steampowered.com/app/220'