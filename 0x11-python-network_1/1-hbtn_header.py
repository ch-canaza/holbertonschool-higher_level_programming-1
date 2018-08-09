#!/usr/bin/python3
'''   '''
import urllib.request as req
from sys import argv
if __name__ == "__main__":
    with req.urlopen(req.Request(argv[1])) as response:
        print(response.headers.get('X-Request-Id'))
