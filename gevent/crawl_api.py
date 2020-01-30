import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import requests
import json

def fetch(pid):
    response = requests.get('http://api.open-notify.org/astros.json')
    json_result = response.json()
    datetime = json_result['people'][0]['name']

    print('Process %s: %s' % (pid, datetime))
    return json_result['people'][0]['name']

def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
