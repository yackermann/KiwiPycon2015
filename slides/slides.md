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
---
.right-section[
### Reasons
]
# Research wise
## Practice your skills, play with technologies, test how much of a dick can you be to a website.
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
.right-section[
### \#1 Connect
]

# UTF-8 EVERYTHING YOU MUST



---
class: left, center

.right-section[
### \#1 Connect
]

# You should get something like this:
```shell
$ py practice.py 
b\'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" 
lang="en-NZ"><head><meta content="/images/google_favicon_128.png" 
itemprop="image"><title>Google</title...
```

---
class: left, center

.right-section[
### \#1 Connect
]

# You should get something like this:
```shell
$ py practice.py 
b\'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" 
lang="en-NZ"><head><meta content="/images/google_favicon_128.png" 
itemprop="image"><title>Google</title...
```

# That is webpage source!

---
.right-section[
### \#1 Connect
]

# Post requests:

## Go to [`http://postcatcher.in/`](http://postcatcher.in/) and get your self a link

---
class: left, center

.right-section[
### \#1 Connect
]

### Post request

## Code:

```python
import urllib.request as request
import urllib.parse as parse

url = 'http://postcatcher.in/catchers/TheUniqueID'

# Post request body
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

### Post request

## Code:
```shell
$ py practice.py 
b'Created'
```

---
class: left, center

.right-section[
### \#1 Connect
]

### Post request

## Code:
```shell
$ py practice.py 
b'Created'
```

# You should get something like this:
![Post request example](images/post.example.png)


---
class: left, center

.right-section[
### \#1 Connect
]

### Get request

## Code:

```python
import urllib.request as request
import urllib.parse as parse

url = 'https://www.google.co.nz/'

body = {
    'hl': 'ko' # Change language to Korean
}

# Encode POST request body
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
$ py practice.py...
```

---
class: left, center
.right-section[
### \#1 Connect
]

```shell
$ py practice.py 
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
# They want you to use it. 
# They don't want you to do the web-parsing!

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

# So lets fool google by setting our self a User-Agent HEADER

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

# Copy your `User-Agent`

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

# Now you should get

```shell
$ practice.py
<!doctype html><html itemscope="" itemtype="http://schema.org/SearchResultsPage" lang="en-NZ">
<head><meta content="/images/google_favicon_128.png" itemprop="image">
<meta content="origin" id="mref" name="referrer"><title>Monthy Python - Google Search</title>
```

