name: inverse
layout: true
class: center, middle, inverse

---
#Web-parsing/scraping/stripping
---
##Web-parsing/scraping/stripping
#...or that thing that you do when there is no API.
---
.right-section[
### Intro
]

# Yuriy Ackermann
## [keybase.io/niemand](https://keybase.io/niemand) 
## [github.com/herrniemand](https://github.com/herrniemand) 

---

# Reasons
---
.right-section[
### Reasons
]
# No API
## Most of the websites simply do not provide API.
---
.right-section[
### Reasons
]
# API Limitations
## Low request quota, high prices, bad API.
### Hello to wikipedia, and thanks for HTML content! Really useful!
---
.right-section[
### Reasons
]
# Research wise
## Practice your skills, play with technologies, test how much of a dick can we be to a website.
---
.right-section[
### Reasons
]
## Why not?
# Why not!
---
# Tutorial plan
---
.right-section[
### Tutorial plan
]
# 1. Connect
## URLLIB
---
.right-section[
### Tutorial plan
]
## 1. Connect
### URLLIB

# 2. Parse
## BeautifulSoup4
---
.right-section[
### Tutorial plan
]
## 1. Connect
### URLLIB (20 min)

## 2. Parse
### BeautifulSoup4 (40 min)

# 3. Parallelize
## Server/Client parser implementation (60m - 75min)
---
.right-section[
### Tutorial plan
]
## 1. Connect
### URLLIB (20 min)

## 2. Parse
### BeautifulSoup4 (40 min)

## 3. Parallelize
### Server/Client parser implementation (60m - 75min)

# 4. Q/A and Bonus

---
# \#1 Connect
---
.right-section[
### \#1 Connect
]
## To connect we will use `urllib`. A standard python url handling library.

## In python 3 it was moved to two separate modules `urllib.request` and `urllib.parse`

---
class: left, center

.right-section[
### \#1 Connect
]

# Example
## Lets try to load `google.com`

```python
import urllib.request as request

data = request.urlopen('https://google.com/')

print(data.read().decode('utf-8'))
```

---
class: left, center

.right-section[
### \#1 Connect
]

# You should get something like this:
```shell
$ python3 practice.py 
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" 
lang="en-NZ"><head><meta content="/images/google_favicon_128.png" 
itemprop="image"><title>Google</title...
```

---
.right-section[
### \#1 Connect
]

# UTF-8 EVERYTHING YOU MUST

## `str.encode('utf-8')`
## `str.decode('utf-8')`

---
class: left, center

.right-section[
### \#1 Connect
]

# You should get something like this:
```shell
$ python3 practice.py 
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" 
lang="en-NZ"><head><meta content="/images/google_favicon_128.png" 
itemprop="image"><title>Google</title...
```

# That is webpage source!

---
.right-section[
### \#1 Connect
]

# POST requests

---
.right-section[
### \#1 Connect
]

## Go to [`http://postcatcher.in/`](http://postcatcher.in/) and get your self a link

---
class: left, center

.right-section[
### \#1 Connect
]

### POST request

## Code:

```python
import urllib.request as request
import urllib.parse as parse

url = 'http://postcatcher.in/catchers/TheUniqueID'

# POST request body
body = {
    'username': 'example',
    'password' : 'examplePassword'
}

# Encode POST request body
data = parse.urlencode(body)
data = data.encode('utf-8')

req = request.Request(url, data)
resp = request.urlopen(req)

print(resp.read().decode('utf-8'))
```
---
class: left, center

.right-section[
### \#1 Connect
]

### POST request

## Code:
```shell
$ python3 practice.py 
Created
```

---
class: left, center

.right-section[
### \#1 Connect
]

### POST request

## Code:
```shell
$ python3 practice.py 
Created
```

# We should get something like this:
![POST request example](images/post.example.png)


---
.right-section[
### \#1 Connect
]
# GET requests

---
class: left, center

.right-section[
### \#1 Connect
]

### GET request

## Lets load Korean version of google by adding GET 
## Code:

```python
import urllib.request as request
import urllib.parse as parse

url = 'https://www.google.co.nz/'

body = {
    'hl': 'ko' # Change language to Korean
}

# Encode GET request body
data = parse.urlencode(body)

req = request.Request(url + '?' + data)
resp = request.urlopen(req)

print(resp.read().decode('utf-8'))
```

---

.right-section[
### \#1 Connect
]

# POST vs GET

---
.right-section[
### \#1 Connect
]

## POST vs GET
# GET - Requests data from a specified resource

---
.right-section[
### \#1 Connect
]

## POST vs GET
# GET - Requests data from a specified resource
# POST - Submits data to be processed to a specified resource

---
class: left, center
.right-section[
### \#1 Connect
]

# If we want to get google search result, we can simply do GET request of the search page
```python
import urllib.request as request
import urllib.parse as parse

url = 'https://google.com/search'

body = {
    'q': 'Monthy Python'
}

# Encode POST request body
data = parse.urlencode(body)

req = request.Request(url + '?' + data)
resp = request.urlopen(req)

print(resp.read().decode('utf-8'))
```

---
class: left, center
.right-section[
### \#1 Connect
]

```shell
$ python practice.py...
```

---
class: left, center
.right-section[
### \#1 Connect
]

```shell
$ python3 practice.py 
Traceback (most recent call last):
  File "practice.py", line 3, in <module>
    data = request.urlopen('https://google.com/search?q=test')
  File "/usr/lib/python3.4/urllib/request.py", line 153, in urlopen
    return opener.open(url, data, timeout)
  File "/usr/lib/python3.4/urllib/request.py", line 461, in open
    response = meth(req, response)
  File "/usr/lib/python3.4/urllib/request.py", line 571, in http_response
    'http', request, response, code, msg, hdrs)
  File "/usr/lib/python3.4/urllib/request.py", line 493, in error
    result = self._call_chain(*args)
  File "/usr/lib/python3.4/urllib/request.py", line 433, in _call_chain
    result = func(*args)
  File "/usr/lib/python3.4/urllib/request.py", line 676, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "/usr/lib/python3.4/urllib/request.py", line 461, in open
    response = meth(req, response)
  File "/usr/lib/python3.4/urllib/request.py", line 571, in http_response
    'http', request, response, code, msg, hdrs)
  File "/usr/lib/python3.4/urllib/request.py", line 499, in error
    return self._call_chain(*args)
  File "/usr/lib/python3.4/urllib/request.py", line 433, in _call_chain
    result = func(*args)
  File "/usr/lib/python3.4/urllib/request.py", line 579, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 403: Forbidden
```

# WAT???

---

.right-section[
### \#1 Connect
]

# Sites like google have an API.
# They want us to use it. 
# They don't want us to do the web-parsing!

---

.right-section[
### \#1 Connect
]

# But how do they know that you are a ROBOT?


---
.right-section[
### \#1 Connect
]

# Headers

---

.right-section[
### Definition
]

# HTTP message HEADERS are used to precisely describe the resource being fetched or the behavior of the server or the client. 
### [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

---
.right-section[
### \#1 Connect
]

# Good example of a HEADER is 
# `User-Agent`

---
.right-section[
### \#1 Connect
]

# My chromium header:
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36`

---
.right-section[
### \#1 Connect
]

# Every browser sends `User-Agent` header to the server.

---

.right-section[
### \#1 Connect
]

# But not our script

---
.right-section[
### \#1 Connect
]

# And thats how google knows that you are a BOT.

---
.right-section[
### \#1 Connect
]

# So lets fool google by setting our self a `User-Agent` HEADER

---
class: left
.right-section[
### \#1 Connect
]

# In the browser open dev-tools:

## * Right-click -> Inspect Element

## * Got to Network tab

## * Select any of the requests and find in the request properties `User-Agent`

---
class: left
.right-section[
### \#1 Connect
]

![User-Agent Chrome](images/user-agent.ch.example.png)
![User-Agent FireFox](images/user-agent.ff.example.png)

---
class: left
.right-section[
### \#1 Connect
]

## Copy your `User-Agent`

```python
import urllib.request as request
import urllib.parse as parse

url = 'https://google.com/search'

headers = {
  'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'
}

body = {
    'q': 'Monthy Python'
}

# Encode POST request body
data = parse.urlencode(body)

req = request.Request(url + '?' + data, headers=headers)
resp = request.urlopen(req)

print(resp.read().decode('utf-8'))
```

---
class: left
.right-section[
### \#1 Connect
]

# Now we should get

```shell
$ python3 practice.py
<!doctype html><html itemscope="" itemtype="http://schema.org/SearchResultsPage" lang="en-NZ">
<head><meta content="/images/google_favicon_128.png" itemprop="image">
<meta content="origin" id="mref" name="referrer"><title>Monthy Python - Google Search</title>
```

---
# This section was proudly sponsored by *Irish music*...

<iframe width="100%" height="50%" src="https://www.youtube.com/embed/qGyPuey-1Jw?list=RDMZ35SOU9HTM" frameborder="0" allowfullscreen></iframe>

# Irish music, *Bímis ar meisce, agus ríomhchláraithe*

---
# Stripping

---

# I mean Parsing...

---

# ...or Scraping

---
.right-section[
### \#2 Stripping
]

# Understanding HTML and CSS

---

.right-section[
### Definitions
]

# HTML
## HyperText Markup Language, is the standard markup language used to create web pages.

---

.right-section[
### Definitions
]

# CSS
## Cascading Style Sheets, is a style sheet language used for describing the look and formatting of a document written in a markup language

---
class: left

.right-section[
### \#2 Stripping
]

# HTML Example

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Example</title>
    </head>
    <body>
        <section id="content">
            <article class="tooltip head"></article>
            <article class="left head" data-type="special"></article>
            <article class="right head"></article>
        </section>
    </body>
</html>
```

---
class: left

.right-section[
### \#2 Stripping
]

# HTML Element/Tag

```html
...
        <title>Example</title> 
...
```

---
class: left

.right-section[
### \#2 Stripping
]

# HTML id
## In HTML/CSS id is unique.

```html
...
        <section id="content">
            ...
        </section>
...
```

---
class: left

.right-section[
### \#2 Stripping
]

# HTML Classes
## In HTML/CSS class is not unique, and there could be more then one class per element.

```html
...
            <article class="tooltip head"></article>
            <article class="left head" data-type="special"></article>
            <article class="right head"></article>
...
```

---
class: left

.right-section[
### \#2 Stripping
]

# HTML Attributes
## Class, id are SPECIAL attributes. When we are generally talking about attributes in web development, we generally mean "Any attribute but class or id". If we talk about class/id, we mean value of class/id attribute.
```html
...
            <article class="left head" data-type="special"></article>
...
```

---
class: left

.right-section[
### \#2 Stripping
]

# CSS Selectors
# `tag`
# `#id`
# `.class`

---
class: left
.right-section[
### \#2 Stripping
]

#HTML DOM
![HTML DOM](images/dom.example.png)

---
class: left
.right-section[
### \#2 Stripping
]

# BeautifulSoup4

## You didn't write that awful page. You're just trying to get some data out of it. Beautiful Soup is here to help. Since 2004, it's been saving programmers hours or days of work on quick-turnaround screen scraping projects.

## `pip3 install beautifulsoup4`

---

class: left
.right-section[
### \#2 Stripping
]

# Back to our code:

```python
import urllib.request as request
import urllib.parse as parse

url = 'https://google.com/search'

headers = {
  'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'
}

body = {
    'q': 'Monthy Python'
}

# Encode POST request body
data = parse.urlencode(body)

req = request.Request(url + '?' + data, headers=headers)
resp = request.urlopen(req)

print(resp.read().decode('utf-8'))
```

---

class: left
.right-section[
### \#2 Stripping
]

## Lets create function `prepare` and import `BeautifulSoup`...

```python
from bs4 import BeautifulSoup

...

def prepare( data ):
    soup = BeautifulSoup(data, 'html.parser')
    title = soup.find('title').text
    return title
```

---
class: left
.right-section[
### \#2 Stripping
]

## ...and parse google.com title
```python
...
htmlContent = resp.read().decode('utf-8')
print(prepare(htmlContent))
...
```

## We should get something like this:
```shell
$ python3 practice.py
Google
```

---

.right-section[
### \#2 Stripping
]

# The End.

---
.right-section[
### \#2 Stripping
]

# Joking

---
.right-section[
### \#2 Stripping
]

# Parsing Steam

---
.right-section[
### \#2 Stripping
]

# Why Steam? Steam has an API?

---
.right-section[
### \#2 Stripping
]

# Because I already done it, and because it has enough *unforeseen pitfalls*.

---
.right-section[
### \#2 Stripping
]

# Lets look for example at HL2 on Steam
## [http://store.steampowered.com/app/220](http://store.steampowered.com/app/220)

## P.S. Where is HL3 Gaben!!!

### 
---
.right-section[
### \#2 Stripping
]

![Steam Example](images/steam.example.png)

---
class: left
.right-section[
### \#2 Stripping
]
.center[
# We have
]
## Name 
## Price(amount and currency) 
## Rating(total and median) 
## Tags
## AppID(220)

---
.right-section[
### \#2 Stripping
]

# Why are we not doing *genre*, *publisher* and *release date*?

---
.right-section[
### \#2 Stripping
]

# Because the way block done, we need a lot of regex in which I, sadly, suck.
# We going for basics today. 

---
class: left
.right-section[
### \#2 Stripping
]
## Object model
```python
game = {
    'appid'    : 0,
    'name'     : '',
    'price'    : 0.0,
    'currency' : '',
    'tags'     : [],
    'rating'   : {
        'total': 0,
        'count': 0
    }
}
```
---
class: left
.right-section[
### \#2 Stripping
]

## Add model to our soup, and comment title for now
```python
def prepare( data ):
    soup  = BeautifulSoup(data, 'html.parser')
    # title = soup.find('title').text
    game = {
        'appid'    : 0,
        'name'     : '',
        'price'    : 0.0,
        'currency' : '',
        'tags'     : [],
        'rating'   : {
            'total': 0,
            'count': 0
        }
    }
    return game
```

---
.right-section[
### \#2 Stripping
]

# BS - BeautifulSoup, not BullShit
---
.right-section[
### \#2 Stripping
]
# BS4

## `.find()` - Return only the first child of this Tag matching the given criteria.
## `.find_all()` -  Extracts a list of Tag objects that match the given criteria.

---
.right-section[
### \#2 Stripping
]
# Name

## Lets go back to [http://store.steampowered.com/app/220](http://store.steampowered.com/app/220)

---
.right-section[
### \#2 Stripping
]

## Right-click the name -> Inspect element
![Element inspection example](images/el.inspect.example.png)

---
.right-section[
### \#2 Stripping
]

## Right-click the name -> Inspect element
![Element inspection example](images/el.inspect.example.png)

## As we can see, the name is in tag `div` and its class `apphub_AppName`

---
class: left
.right-section[
### \#2 Stripping
]

```python
def prepare( data ):
    soup  = BeautifulSoup(data, 'html.parser')
    # title = soup.find('title').text
    game = {
        'appid'    : 0,
        'name'     : soup.find('div', {'class': 'apphub_AppName'}),
        'price'    : 0.0,
        'currency' : '',
        'tags'     : [],
        'rating'   : {
            'total': 0,
            'count': 0
        }
    }
    return game
```

---
class: left
.right-section[
### \#2 Stripping
]
## If we will try now to run our parser

```shell
$ python3 practice.py
{'rating': {'total': 0, 'count': 0}, 'name': <div class="apphub_AppName">Half-Life 2</div>, 'tags': [], 'appid': 0, 'price': 0.0, 'currency': ''}
```

---
class: left
.right-section[
### \#2 Stripping
]
## If we will try now to run our parser

```shell
$ python3 practice.py
{'rating': {'total': 0, 'count': 0}, 'name': <div class="apphub_AppName">Half-Life 2</div>, 'tags': [], 'appid': 0, 'price': 0.0, 'currency': ''}
```

## We got name tag

## It doesn't matter that it is a tag object. Right now we are simply getting elements.

---
class: left
.right-section[
### \#2 Stripping
]
## Lets continue do it for everything else
```python
def prepare( data ):
    soup  = BeautifulSoup(data, 'html.parser')
    # title = soup.find('title').text
    game = {
        'appid'    : 0,
        'name'     : soup.find('div', {'class': 'apphub_AppName'}),
        'price'    : soup.find('div', {'class': 'game_purchase_price price'}),
        'currency' : soup.find('div', {'class': 'game_purchase_price price'}),
        'tags'     : [],
        'rating'   : {
            'count' : soup.find('meta', { 'itemprop' : 'ratingValue' }),
            'total' : soup.find('meta', { 'itemprop' : 'reviewCount' })
        }
    }
    return game
```

---
class: left
.right-section[
### \#2 Stripping
]

## There more then one tag, so we want to find them all with `.find_all()`

---
class: left
.right-section[
### \#2 Stripping
]

## Example of a steam tag:
```html
<a href="..." class="app_tag" style="">Sci-fi</a>
```

---
class: left
.right-section[
### \#2 Stripping
]

```python
...
'tags'     : soup.find_all('a', {'class': 'app_tag'})
...
```
---
class: left
.right-section[
### \#2 Stripping
]

## Final code
```python
def prepare( data ):
    soup  = BeautifulSoup(data, 'html.parser')
    # title = soup.find('title').text
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
```

---
class: left
.right-section[
### \#2 Stripping
]

## Result
```shell
$ python3 practice.py
{'tags': [<a... TOO MUCH CONTENT TO PUT IN A SLIDE
```


---
.right-section[
### \#2 Stripping
]
## Thats cool, we made function that finds and returns HTML elements, now we need data out of that.

---
.right-section[
### \#2 Stripping
]
## Thats cool, we made function that finds and returns HTML elements, now we need data out of that.

# Lets make a `cook()` function for that!
---
class: left
.right-section[
### \#2 Stripping
]

```python
def cook(content):
    pass
```

---
class: left
.right-section[
### \#2 Stripping
]

## Our cook function will use the same game model as prepare, so lets just copy it over, and access to old data corresponding elements

```python
def cook( data ):
    game = {
        'appid'     : data['appid'],
        'name'      : data['name'],
        'price'     : data['price'],
        'currency'  : data['currency'],
        'tags'      : data['tags'],
        'rating'    : {
            'total' : data['rating']['total'],
            'count' : data['rating']['count']
        }
    }
    return game

```
---
class: left
.right-section[
### \#2 Stripping
]

## From *Name*, *Price*, *Curerncy* we need just inner content. We can get that by accessing `.text` attribute

```python
...
        'name'      : data['name'].text,
        'price'     : data['price'].text,
        'currency'  : data['currency'].text,
...
```

---
class: left
.right-section[
### \#2 Stripping
]

## *Tags* are a list of HTML tags. We can get their inner by iterating through the list and accessing each tags with `.text` attribute.

```python
...
        'tags'      : [ tag.text for tag in data['tags'] ],
...
```

---
class: left
.right-section[
### \#2 Stripping
]

## If we look at rating *meta* tags

```html
...
            <meta itemprop="reviewCount" content="26072">
            <meta itemprop="ratingValue" content="10">
...
```

## We can access `content` attribute of meta tags as dictionary:
```python
        'rating'    : {
            'total' : data['rating']['total']['content'],
            'count' : data['rating']['count']['content']
        }
```
---
class: left
.right-section[
### \#2 Stripping
]

## We should end up with something like this
```python
def cook( data ):
    game = {
        'appid'     : data['appid'],
         'name'     : data['name'].text,
        'price'     : data['price'].text,
        'currency'  : data['currency'].text,
        'tags'      : [ tag.text for tag in data['tags'] ],
        'rating'    : {
            'total' : data['rating']['total']['content'],
            'count' : data['rating']['count']['content']
        }
    }
    return game
```

---
class: left
.right-section[
### \#2 Stripping
]

## Lets test it out:

```python
print(cook(prepare(htmlContent)))
```


```shell
$ python3 practice.py
{'rating': {'count': '10', 'total': '26072'}, 'currency': 
'\r\n\t\t\t\t\t\t\tNZ$ 11.99\t\t\t\t\t\t', 
'price': '\r\n\t\t\t\t\t\t\tNZ$ 11.99\t\t\t\t\t\t', 'appid': 0, 'tags': ['\r\n\t\t\t\t\t\t\t\t\t\t\t\tFPS\t\t\t\t\t\t\t\t\t\t\t\t',
'\r\n\t\t\t\t\t\t\t\t\t\t\t\tAction\t\t\t\t\t\t\t\t\t\t\t\t',
'\r\n\t\t\t\t\t\t\t\t\t\t\t\tSci-fi\t\t\t\t\t\t\t\t\t\t\t\t',
'\r\n\t\t\t\t\t\t\t\t\t\t\t\tClassic\t\t\t\t\t\t\t\t\t\t\t\t',
'\r\n\t\t\t\t\t\t\t\t\t\t\t\tSingleplayer\t\t\t\t\t\t\t\t\t\t\t\t', '\r\n\t\t\t\t\t\t\t\t\t\t\t\tStory Rich\t\t\t\t\t\t\t\t\t\t\t\t',
```

---
class: left
.right-section[
### \#2 Stripping
]

## So we finished right?
## I mean we can just simply stick **for loop** and bruteforce entire steam?

---
class: left
.right-section[
### \#2 Stripping
]

## Lets change url to [http://store.steampowered.com/app/7340](http://store.steampowered.com/app/7340)

```python
url = 'http://store.steampowered.com/app/7340'
```

---
class: left
.right-section[
### \#2 Stripping
]

## Lets change url to [http://store.steampowered.com/app/7340](http://store.steampowered.com/app/7340)

```python
url = 'http://store.steampowered.com/app/7340'
```

```shell
$ python3 practice.py
...
```
---
class: left
.right-section[
### \#2 Stripping
]

## Lets change url to [http://store.steampowered.com/app/7340](http://store.steampowered.com/app/7340)

```python
url = 'http://store.steampowered.com/app/7340'
```

```shell
$ python3 practice.py
Traceback (most recent call last):
  File "practice.py", line 53, in <module>
    print(cook(prepare(htmlContent)))
  File "practice.py", line 36, in cook
    'price'     : data['price'].text,
AttributeError: 'NoneType' object has no attribute 'text'

```
# Shit...
---
.right-section[
### \#2 Stripping
]

# Unforeseen Pitfalls 

---
.right-section[
### \#2 Stripping
]

## We currently tested our code on the *perfect* example.

---
.right-section[
### \#2 Stripping
]

## We currently tested our code on the *perfect* example.

## It has Name, Price, Tags etc.

---
.right-section[
### \#2 Stripping
]

## We currently tested our code on the *perfect* example.

## It has Name, Price, Tags etc.

## But not all games pages are *perfect*

---
.right-section[
### \#2 Stripping
]

# Price
![Price](images/price.p.example.png)

.left[
[http://store.steampowered.com/app/220](http://store.steampowered.com/app/220)
]

# Free to play
![Free to Play](images/f2p.p.example.png)

.left[
[http://store.steampowered.com/app/440](http://store.steampowered.com/app/440)
]

# No price at all
![No price at all](images/noprice.p.example.png)

.left[
[http://store.steampowered.com/app/7340](http://store.steampowered.com/app/7340)
]

---
.right-section[
### \#2 Stripping
]

# Region locked games

![Region locked games](images/region.unavailable.example.png)

---
.right-section[
### \#2 Stripping
]
# 404 redirection to main page
## [http://store.steampowered.com/app/230](http://store.steampowered.com/app/230)
---
.right-section[
### \#2 Stripping
]

## So writing parsing, is simply a process of proving *Murphys Law*.
## If anything can go wrong, it, bloody, will!

---
.right-section[
### \#2 Stripping
]

# Possible faults

---
class: left
.right-section[
### \#2 Stripping
]

## GET request. Timeout, DNS, Host Is Down, No Internet 
---
class: left
.right-section[
### \#2 Stripping
]

## GET request. Timeout, DNS, Host Is Down, No Internet 
## Page does not have price, tags, name etc.
---
class: left
.right-section[
### \#2 Stripping
]

## GET request. Timeout, DNS, Host Is Down, No Internet 
## Page does not have price, tags, name etc.
## Error page -> Region locked games
---
class: left
.right-section[
### \#2 Stripping
]

## GET request. Timeout, DNS, Host Is Down, No Internet 
## Page does not have price, tags, name etc.
## Error page -> Region locked games
## 404 Error. Redirection to main page

---
class: left
.right-section[
### \#2 Stripping
]

## GET request. Timeout, DNS, Host Is Down, No Internet 
## Page does not have price, tags, name etc.
## Error page -> Region locked games
## 404 Error. Redirection to main page
## Cosmic radiation in a form of HEP(High Energetic Particles), e.g. Muons.

---
class: left
.right-section[
### \#2 Stripping
]

## GET request. Timeout, DNS, Host Is Down, No Internet 
## Page does not have price, tags, name etc.
## Error page -> Region locked games
## 404 Error. Redirection to main page
## Cosmic radiation in a form of HEP(High Energetic Particles), e.g. Muons.
## Quantum fluctuations, and Casimir effect on electron movement in the processor.

---
class: left
.right-section[
### \#2 Stripping
]

## GET request. Timeout, DNS, Host Is Down, No Internet 
## Page does not have price, tags, name etc.
## Error page -> Region locked games
## 404 Error. Redirection to main page
## Cosmic radiation in a form of HEP(High Energetic Particles), e.g. Muons.
## Quantum fluctuations, and Casimir effect on electron movement in the processor.
## Other

---
class: left
.right-section[
### \#2 Stripping
]

## Lets move GET request to a separate function and wrap it with *try/except*
## As addition we add timeout of *2 seconds*

```python
def get(url):
    try:
        headers = {
          'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'
        }

        req = request.Request(url, headers=headers)
        resp = request.urlopen(req, timeout=2)

        return { 'ok': True, 'data': resp.read().decode('utf-8')}
    except Exception as e:
        return { 'ok': False, 'error': str(e)}
```

---
class: left
.right-section[
### \#2 Stripping
]

# Lets test it on *perfect example*

```python
response = get('http://store.steampowered.com/app/220')
if response['ok']:
    print(cook(prepare(response['data'])))
```

```shell
$ python3 practice.py
{'tags': ['\r\n\t\t\t\t\t\t\t\t\t\t\t\tFPS\t\t\t\t\t\t\t\t\t\t\t\t'...
```

---
class: left
.right-section[
### \#2 Stripping
]

## ~~GET request. Timeout, DNS, Host Is Down, No Internet~~
## Page does not have price, tags, name etc.
## Error page -> Region locked games
## 404 Error. Redirection to main page

---
class: left
.right-section[
### \#2 Stripping
]
.center[
## Currently we have two problems with our content.
]
---
class: left
.right-section[
### \#2 Stripping
]
.center[
### Currently we have two problems with our content.
]
## Its not fail-safe. That means that if something is missing and we try to get its content, we get exception.

---
class: left
.right-section[
### \#2 Stripping
]
.center[
### Currently we have two problems with our content.
]
## Its not fail-safe. That means that if something is missing and we try to get its content, we get exception. 

## It is full of rubbish like *tabs* and *spaces*

---
class: left
.right-section[
### \#2 Stripping
]

## Lets create format function for name, price, currency, tags entries in `cook()`
```python
def cook( data ):
    def name(item):
        pass
    def price(item):
        pass
    def currency(item):
        pass
    def tag(item):
        pass
    game = {
        'appid'     : data['appid'],
        'name'      : data['name'].text,
        'price'     : data['price'].text,
        'currency'  : data['currency'].text,
        'tags'      : [ tag.text for tag in data['tags'] ],
        'rating'    : {
            'total' : data['rating']['total']['content'],
            'count' : data['rating']['count']['content']
        }
    }
    return game
```

---
class: left
.right-section[
### \#2 Stripping
]

## We need to make sure that entries are not `None` before accessing them
```python
...
    def name( item ):
        if item != None:
            return item.text
        else:
            return ''
```

---
class: left
.right-section[
### \#2 Stripping
]

## Price and currency can be *Free to play* as well, so we need to account that as well

```python
    def price( item ):
        if item != None:
            if 'Free to play' in item.text:
                return 0.0
            else:
                return item.text
        else:
            return 0.0

    def currency( item ):
        if item != None:
            if 'Free to play' in item.text:
                return ''
            else:
                return item.text
        else:
            return ''
```

---
class: left
.right-section[
### \#2 Stripping
]

## Same for ratings
```python
...
    def rating( item ):
        if item != None:
            return item['content']
        else:
            return 0
...
```

---
class: left
.right-section[
### \#2 Stripping
]

## Lets parse the values through the handling functions

```python
...
    game = {
        'appid'     : data['appid'],
        'name'      : name(data['name']),
        'price'     : price(data['price']),
        'currency'  : currency(data['currency']),
        'tags'      : [ tag.text for tag in data['tags'] ],
        'rating'    : {
            'total' : rating(data['rating']['total']),
            'count' : rating(data['rating']['count'])
        }
    }
```

---
class: left
.right-section[
### \#2 Stripping
]
## Not lets test it with *Bad* game
```python
response = get('http://store.steampowered.com/app/7340')
```

```shell
$ python3 practice.py
{'tags': ['\r\n\t\t\t\t\t\t\t\t\t\t\t\tPuzzle\t\t\t\t\t\t\t\t\t\t\t\t'], 'appid': 0, 'currency': '', 'rating': {'total': '4', 'count': '7'}, 'price': 0.0, 'name': 'Azada'}
```

---
class: left
.right-section[
### \#2 Stripping
]
.center[
### Currently we have two problems with our content.
]
## ~~Its not fail-safe. That means that if something is missing and we try to get its content, we get exception.~~

## It is full of rubbish like *tabs* and *spaces*

---
class: left
.right-section[
### \#2 Stripping
]

## For cleaning tabs, spaces and non-numeric characters we will create `clean()` function that will do regex substitution

```python
import re

...

def clean( content, form ):
    expressions = {
        'tabs' : r'[\n|\t|\r]',
        'numbers' : r'[^0-9\.]'
    }
    regex = re.compile(expressions[form])
    return regex.sub('', content)
```

---
class: left
.right-section[
### \#2 Stripping
]

## Cleaning name and price outputs
```python
...
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
...
        'tags'      : [ clean(tag.text, 'tabs') for tag in data['tags'] ],
...
```

---
class: left
.right-section[
### \#2 Stripping
]

## The currency is a quiet a problem. 
## It can be just symbol `£`, or text with symbol `NZ$`, and because of *Magic* python regex, we can not do unicode ranges, so we simply have to do an array of currency symbols in a regex.

```python
    def currency( item ):
        if item != None:
            if 'Free to play' in item.text:
                return ''
            else:
                return re.findall(r'[A-Za-z]*[$¢£¤¥֏؋৲৳৻૱௹฿៛€]', item.text)
        else:
            return ''

```
---
class: left
.right-section[
### \#2 Stripping
]

## Final code
```python
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
```
---
class: left
.right-section[
### \#2 Stripping
]

## Lets test it out

```shell
$ python3 practice.py 
{'currency': ['NZ$'], 'appid': 0, 'price': '11.99', 'name': 'Half-Life 2', 
'rating': {'total': '26081', 'count': '10'}, 'tags': ['FPS', 'Action', 'Sci-fi'
, 'Classic', 'Singleplayer', 'Story Rich', 'Shooter', 'Adventure', 
'First-Person', 'Dystopian ', 'Atmospheric', 'Great Soundtrack', 'Zombies', 
'Aliens', 'Silent Protagonist', 'Physics', 'Moddable', 'Horror', 'Puzzle', 
'Multiplayer']}
```

---
class: left
.right-section[
### \#2 Stripping
]

## ~~GET request. Timeout, DNS, Host Is Down, No Internet~~
## ~~Page does not have price, tags, name etc.~~
## Error page -> Region locked games
## 404 Error. Redirection to main page

---

class: left
.right-section[
### \#2 Stripping
]

## Do you still remember the `title` block in a `prepare()` function that we commented at the beginning?

```python
    # title = soup.find('title').text
```
---

class: left
.right-section[
### \#2 Stripping
]

## Do you still remember the `title` block in a `prepare()` function that we commented at the beginning?

```python
    # title = soup.find('title').text
```

## When there is region lock or any serious error, the title have `Site Error` in its title. And because we know that title is **always** there, we can simply ignore check. 

```python
    ...
    if not 'Site Error' in soup.find('title').text:
        game = {
            'appid'    : 0,
            ...
        }
```

---
class: left
.right-section[
### \#2 Stripping
]

## ~~GET request. Timeout, DNS, Host Is Down, No Internet~~
## ~~Page does not have price, tags, name etc.~~
## ~~Error page -> Region locked games~~
## 404 Error. Redirection to main page

---
class: left
.right-section[
### \#2 Stripping
]

## So when we get 404 at Steam, we get redirected to main page. 
## So we just need compare original url and returned

---
class: left
.right-section[
### \#2 Stripping
]

## To get access to response url, we simply access url attribute of response
```python
    response.url
```

## So lets return if urls are match

```python
def get(url):
    try:
        headers = {
          'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'
        }

        req = request.Request(url, headers=headers)
        resp = request.urlopen(req, timeout=2)

        return { 
            'ok': True,
            'URLMatch': url == resp.url,
            'data': resp.read().decode('utf-8')
        }
    except Exception as e:
        return { 'ok': False, 'error': str(e)}
...

if response['ok'] and response['URLMatch']:
    print(cook(prepare(response['data'])))
```
---
class: left

## Right now we can simply make *for-loop* and parse all of the steam games.

---
class: left

# But the problems with this are:
## Lots of requests. e.g. 100k to bruteforce steam.

---
class: left

# But the problems with this are:
## Lots of requests. e.g. 100k to bruteforce steam.
## Long time. If request and parsing takes 250ms, we will need around 7 hours to do that.

---
class: left

# But the problems with this are:
## Lots of requests. e.g. 100k to bruteforce steam.
## Long time. If request and parsing takes 250ms, we will need around 7 hours to do that.
## Requests from one ip. Admins can check logs, and as a response provide ban, or 100gb porn archive for your ip address.

---

# Your thoughts right now

![Where is the pizza?](images/where.is.the.pizza.gif)

---
# Well then
![No soup for you](images/no.soup.for.you.gif)

---

# Prize challenge!

![Challenge](images/challenge.gif)

# MUST BE DONE BY END OF \#3 Parallelize
---
# This section was proudly sponsored by *German folk music*

<iframe width="100%" height="50%" src="https://www.youtube.com/embed/8bzziAv9o4w" frameborder="0" allowfullscreen></iframe>

# German music, what a great tool to keep people away from you!

### Yes, I know the songs are about Austria
---
# ~~\#3 Paralelise~~
# ~~\#3 Parallelise~~
# \#3 Parallelize

---
class: left
.right-section[
### \#3 Parallelize
]

## The algorithm:
## We have Server and Client
## Client gets task using GET request to `/get`, Server assigns task to ip and send *task*
## Client does task, and POST data to `/post` Server. Server saves result, and finishes task.

---
.right-section[
### \#3 Parallelize
]

# Server && Client

---
class: left
.right-section[
### \#3 Parallelize
]

## Lets separate our code. 
## `parcer.py` - Anything to do with parsing
## `client.py` - Anything to do with client side
## `server.py` - Anything to do with server side

---
class: left
.right-section[
### \#3 Parallelize
]

## So lets rename `practice.py` to `parser.py`, and move `get()` to `client.py`
```python
#client.py
import urllib.request as request
import urllib.parse   as parse
from parser import *

def get(url):
    try:
        headers = {
          'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'
        }

        req = request.Request(url, headers=headers)
        resp = request.urlopen(req, timeout=2)
        
        return { 
            'ok': True,
            'URLMatch': url == resp.url,
            'data': resp.read().decode('utf-8')
        }
    except Exception as e:
        return { 'ok': False, 'error': str(e)}
```

---
.right-section[
### \#3 Parallelize
]

# Server

---
class: left
.right-section[
### \#3 Parallelize
]

## For server we will user standard python library `http.server`
## Specifically two classes
## `BaseHTTPRequestHandler` and `HTTPServer`

---

class: left
.right-section[
### \#3 Parallelize
]

## *BaseHTTPRequestHandler* does request processing that given by *HTTPServer*.
## Lets make simple HTTP server
```python
from http.server import BaseHTTPRequestHandler, HTTPServer

address = ( '0.0.0.0', 8888 )

server = HTTPServer(address, BaseHTTPRequestHandler)

print('Staring server at', address[0], 'port', address[1])

server.serve_forever()
```

```shell
$ python3 server.py 
Staring server at 0.0.0.0 port 8888
```

---
class: left
.right-section[
### \#3 Parallelize
]

## Now open [http://localhost:8888](http://localhost:8888)

## You should get:
```HTML
Error response

Error code: 501

Message: Unsupported method ('GET').

Error code explanation: 501 - Server does not support this operation.
```

## And console should have something like this
```shell
$ python server.py 
Staring server at 0.0.0.0 port 8888
127.0.0.1 - - [01/Sep/2015 20:39:11] code 501, message Unsupported method ('GET')
127.0.0.1 - - [01/Sep/2015 20:39:11] "GET / HTTP/1.1" 501 -
...
```

---
class: left
.right-section[
### \#3 Parallelize
]

## Currently we are getting error on GET request, this is because GET request is not implemented, so we have to take care of that by expanding *BaseHTTPRequestHandler* class.

## Lets extend *BaseHTTPRequestHandler* class with *HTTPProcessor* class

```python
class HTTPProcessor(BaseHTTPRequestHandler):
    pass
```

---
class: left
.right-section[
### \#3 Parallelize
]

## To handle GET request we need add to *HTTPProcessor* `do_GET()` function
```python
class HTTPProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        print('Getting get request from', self.client_address)

```

## And lets change current processor to new one
```python
#server = HTTPServer(address, BaseHTTPRequestHandler)
server = HTTPServer(address, HTTPProcessor)
```

## Lets test it out again
```shell
$ python3 server.py 
Staring server at 0.0.0.0 port 8888
Getting get request from ('127.0.0.1', 54461)
Getting get request from ('127.0.0.1', 54462)
...
```

---
class: left
.right-section[
### \#3 Parallelize
]

## Currently we can see how client sending us requests, but we are not replying back. 
## When client sends us request, we need to provide some information with our response, such as 
## *status code*, so client knows if we are OK.
## *content-type header*, so client knows what type information it is.
```python
class HTTPProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/plain')
        self.end_headers()

        print('Getting get request from', self.client_address)
```

---
class: left
.right-section[
### \#3 Parallelize
]

## Now we can send client some data
```python
class HTTPProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/plain')
        self.end_headers()

        self.wfile.write('Hello World!'.encode('utf-8'))

        print('Getting get request from', self.client_address)
```
# UTF-8 EVERYTHING YOU MUST!

## You should get something like this
![Response example](images/resp.simple.example.png)

---
class: left
.right-section[
### \#3 Parallelize
]

## Parsing Steam is a big job. 
## Since steam library is over 8000 game and around 20000 DLCs, it is reasonable to brute-force up to 1000000. 
## So it will take us 100000 request.(Because appIDs ALWAYS finish with 0, so it is step 10)
## Lets say we make 4 requests per second that still will be ~7 hours of brute-forcing. 
## So we need to split the task on to small chunks, and do them parallel on multiple VMs.

---
class: left
.right-section[
### \#3 Parallelize
]

# Task List

---
class: left
.right-section[
### \#3 Parallelize
]

## For parsing Steam we will need very simple task manager...

---
class: left
.right-section[
### \#3 Parallelize
]

## And because writing task list is the most possibly boring thing to do, please download it from here:

[https://raw.githubusercontent.com/herrniemand/KiwiPycon2015/master/tasklist.py](https://raw.githubusercontent.com/herrniemand/KiwiPycon2015/master/tasklist.py)

---
class: left
.right-section[
### \#3 Parallelize
]

```shell
class TaskList(builtins.object)
 |  TaskList Class
 |  
 |  Methods defined here:
 |  
 |  __init__(self)
 |  
 |  addTask(self, id, r)
 |      Adds new Task to TaskList
 |  
 |  completeTask(self, ip, data)
 |      Completes task specified by ip address
 |  
 |  exportData(self)
 |      Exports all data to JSON file
 |  
 |  failTask(self, ip)
 |      Fails Task, specified by ip address
 |  
 |  getJSON(self, ip)
 |      Return JSON encoded Task, specified by ip address
 |  
 |  getTask(self, ip)
 |      Returns Task from TaskList, specified by ip address
 |  
 |  updateStatus(self, ip)
 |      Updates Task timestamp, specified by ip address
```

---
class: left
.right-section[
### \#3 Parallelize
]

## For the start lets import *Task List*.
```python
...
from tasklist import *
...
manager = TaskList()
```

## Lets add test task
```python
manager.addTask('test', range(0, 100, 10))
```

---
class: left
.right-section[
### \#3 Parallelize
]
## When client does GET request, we want to give him task. So first we need to find clients ip address.
```python
class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        ...
        ip = self.client_address[0]
        ...
```

---
class: left
.right-section[
### \#3 Parallelize
]
## Now lets get the task, and send it to client.
```python
class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        ...
        ip = self.client_address[0]
        ...
        task = manager.getTask(ip)
        self.wfile.write(task.encode('utf-8'))
```

## Now in the browser you should see JSON return
```javascript
{"stop": 100, "start": 0, "step": 10}
```

---
class: left
.right-section[
### \#3 Parallelize
]

## Currently our *content-type* header set to *text/plain*, but we are returning JSON. Lets fix that.
```python
        ...
        self.send_header('content-type','application/json')
        ...
```

---
class: left
.right-section[
### \#3 Parallelize
]

## Back to `client.py`.

## Lets retrieve task from server
```python
...
response = get('http://localhost:8888/')
print(response)
```

## If your server is up
```shell
$ python3 client.py
{'ok': True, 'URLMatch': True, 'data': '{"step": 10, "start": 0, "stop": 100}'}
```

## If it is down
```shell
$ python3 client.py
{'error': '<urlopen error [Errno 111] Connection refused>', 'ok': False}
```

---
class: left
.right-section[
### \#3 Parallelize
]

## If request was successful, then we need to parse JSON from response
```python
import json
...
response = get('http://localhost:8888/')
if response['ok']:
    task = json.loads(response['data'])
```

## The task if simple *range*. It has *start*, *stop*, and *step*. Before we do anything, we need to make sure all of them are exist, and if they are okay, then we can generate *range* instance.
```python
response = get('http://localhost:8888/')
if response['ok']:
    task = json.loads(response['data'])
    if 'start' in task and 'stop' in task and 'step' in task:
        r = range(task['start'], task['stop'], task['step'])
```

---
class: left
.right-section[
### \#3 Parallelize
]

## For bruteforcing we need to write a separate function. It will accept range as an argument and iterate until done.
```python
def bruteforceRange(r):
    for appid in r:
        url = 'http://store.steampowered.com/app/' + str(appid)
        print(url)
```

## Now lets run this function with task range
```python
...
    if 'start' in task and 'stop' in task and 'step' in task:
        r = range(task['start'], task['stop'], task['step'])
        bruteforceRange(r)
...
```

```shell
$ python3 client.py 
http://store.steampowered.com/app/0
http://store.steampowered.com/app/10
http://store.steampowered.com/app/20
http://store.steampowered.com/app/30
http://store.steampowered.com/app/40
http://store.steampowered.com/app/50
http://store.steampowered.com/app/60
http://store.steampowered.com/app/70
http://store.steampowered.com/app/80
http://store.steampowered.com/app/90

```
---
class: left
.right-section[
### \#3 Parallelize
]

## Now we can parse links
```python
def bruteforceRange(r):
    games = []
    for appid in r:
        url = 'http://store.steampowered.com/app/' + str(appid)
        data = get(url)
        if data['ok']:
            if data['URLMatch']:
                precook = prepare(data['data'])
                if precook:
                    dish = cook(precook)
                    games.append(dish)
                    print(dish)
    return games

```

```shell
$ python3 client.py 
Doing http://store.steampowered.com/app/10
{'rating': {'count': '10', 'total': '48631'}, ...

Doing http://store.steampowered.com/app/20
{'rating': {'count': '9', 'total': '1800'}, 'tags':...

Doing http://store.steampowered.com/app/30
{'rating': {'count': '9', 'total': '1610'},...

```

---
class: left
.right-section[
### \#3 Parallelize
]
## Add some requests description
```python
def bruteforceRange(r):
    games = []
    for appid in r:
        url = 'http://store.steampowered.com/app/' + str(appid)
        data = get(url)
        if data['ok']:
            if data['URLMatch']:
                precook = prepare(data['data'])
                if precook:
                    print('Doing', url)
                    dish = cook(precook)
                    games.append(dish)
                else:
                    print('Skipping', url)
            else:
                print('Skipping', url)
        else:
            print('Skipping', url)

    return games
```

---
class: left
.right-section[
### \#3 Parallelize
]

## Lets print the results
```python
...
    if 'start' in task and 'stop' in task and 'step' in task:
        r = range(task['start'], task['stop'], task['step'])
        print(bruteforceRange(r))
...
```

```shell
$ py client.py 
Skipping http://store.steampowered.com/app/0
Doing http://store.steampowered.com/app/10
Doing http://store.steampowered.com/app/20
Doing http://store.steampow...
...
[{'tags': ['Action', 'FPS', 'Multiplayer', 'Classic', 'Shooter', 'Team-Based',
 'Competitive', 'First-Person', 'Tactical', "1990's", 'e-sports', 'PvP', 
 'Strategy', 'Military', '1980s', 'Score Attack', 'Survival', 'Assassin',
  'Ninja', 'Tower Defense'], 'appid': 0, 'name': 'Counter-Strike', 'price': 
  '11.99', 'currency': ['NZ$'], 'rating': {'total'...
```

---
class: left
.right-section[
### \#3 Parallelize
]

## Now we need to post result back to server. To do that we need to write *POST* maker for *client*, and *POST* processor for *server*.
## Client post function is pretty much a copy of GET. Except we need to add `body` to arguments and encode it in request

```python
def post(url, values):
    try:
        headers = {
          'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'
        }

        data = parse.urlencode(values)
        data = data.encode('utf-8')

        req = request.Request(url, data, headers=headers)
        resp = request.urlopen(req, timeout=2)
        
        return { 
            'ok': True,
            'URLMatch': url == resp.url,
            'data': resp.read().decode('utf-8')
        }
    except Exception as e:
        return { 'ok': False, 'error': str(e)}
```
---
class: left
.right-section[
### \#3 Parallelize
]
## Same as we did *GET* request handling with `do_GET()`, we can handle *POST* with `do_POST()`
```python
class HTTPProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
    ....

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type','application/json')
        self.end_headers()

        ip = self.client_address[0]
```

---
class: left
.right-section[
### \#3 Parallelize
]
## To parse *POST* we need to use `cgi` library
```python
        import cgi
        ...
        form = cgi.FieldStorage(
            fp      = self.rfile, 
            headers = self.headers,
            environ = {
                'REQUEST_METHOD' : 'POST',
                'CONTENT_TYPE'   : self.headers['Content-Type'],
            }
        )
```

## Lets print request
```python
        print('Getting post request from', ip, form)
```

---
class: left
.right-section[
### \#3 Parallelize
]

## Testing request
```python
post('http://localhost:8888/', {'username': 'bob'}) #client.py
```

```shell
$ python3 client.py
```

```shell
$ python3 server.py
127.0.0.1 - - [04/Sep/2015 06:54:52] "POST / HTTP/1.1" 200 -
Getting post request from 127.0.0.1 FieldStorage(None, None, [MiniFieldStorage('username', 'bob')])
```

---
class: left
.right-section[
### \#3 Parallelize
]

## When client finish brute-forcing, it will JSON encode data and *POST* it server with *method* *data*
```python
    ...
    if 'start' in task and 'stop' in task and 'step' in task:
        r = range(task['start'], task['stop'], task['step'])
        data = bruteforceRange(r)
        post('http://localhost:8888/', {'method': 'data', 'data': json.dumps(data)})
```

## Server checks if method is defined, and if data is provided 

```python
        ...
        form = cgi.FieldStorage(
            fp      = self.rfile, 
            headers = self.headers,
            environ = {
                'REQUEST_METHOD' : 'POST',
                'CONTENT_TYPE'   : self.headers['Content-Type'],
            }
        )

        if 'method' in form:
            if form['method'].value == 'data':
                if 'data' in form:
                    data = form['data'].value
                
                else:
                    print('No data')
        ...
```

---
class: left
.right-section[
### \#3 Parallelize
]

## And then we try to parse JSON response, if OK we will complete task, else fail.
```python
    ...
    if 'method' in form:
        if form['method'].value == 'data':
            if 'data' in form:
                rawData = form['data'].value
                try:
                    data = json.loads(rawData)
                    manager.completeTask(ip, data)
                    print('Success data')
                except Exception as e:
                    print(e)
                    manager.failTask(ip)
                    print('Failed data')
            else:
                    print('No data')
```
---
class: left
.right-section[
### \#3 Parallelize
]

## Lets remove annoying console logs by redefining `log_message` method in *HTTPProcessor* class
```python

class HTTPProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        ...
    def do_POST(self):
        ...
    def log_message(self, format, *args):
        return
```

---
class: left
.right-section[
### \#3 Parallelize
]

## Lastly we need to add task generator:
```python
was = 0
step = 10
for i in range(2500, 1000000, 2500):
    id = str(was) + '-' + str(i)
    manager.addTask(id, range(was, i, step))
    was = i

address = ( '0.0.0.0', 8888 )
...
```

---
class: left
.right-section[
### \#3 Parallelize
]

## And lets add infinite loop for the client and move start code to the separate function

```python
def StartClient():
    mothership = 'http://localhost:8888/'
    print('Starting client...')
    while True:
        task = ''
        try:
            task = get(mothership)
        except:
            print('Server is down')
            sleep(1)
            continue

        if task['ok']:
            todo = json.loads(task['data'])
            if 'start' in todo and 'stop' in todo and 'step' in todo:
                print('Received task:', todo['start'], 'to', todo['stop'], 'step', todo['step'] )
                r = range(todo['start'], todo['stop'], todo['step'])
 
                data = bruteforceRange(r)
                post(mothership, {'method': 'data', 'data' : json.dumps(data)})
            else:
                print('Not task')
                sleep(1)
        else:
            print('Failed to receive task')
        sleep(1)

StartClient()
```


















---
# This section was proudly sponsored by *French music*

<iframe width="100%" height="50%" src="https://www.youtube.com/embed/zfjm0K1l7AM" frameborder="0" allowfullscreen></iframe>

# French music, what a great way to show how romantic your code is...

---
# \#4 Q/A and Bonus

---
![WE DO IT LIVE](images/we.do.it.live.gif)
---

# The end

---

![Been a pleasure to know ya'll](images/preasure.to.know.yall.gif)

---

## Any grammar, bugs, improvements, please submit pull request
## [https://github.com/herrniemand/KiwiPycon2015](https://github.com/herrniemand/KiwiPycon2015)

---

## Any love/hate messages, and comments please email me
## [ackermann.yuriy@gmail.com](mailto:ackermann.yuriy@gmail.com)

## You can encrypt it with my public key
## [https://keybase.io/niemand/key.asc](https://keybase.io/niemand/key.asc)

---

## Any Best-friends/Face-punching offers
## Please meet at the pub tonight.
