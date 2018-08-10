#!/usr/bin/python3
''' fetches https://intranet.hbtn.io/status '''
import urllib.request as req
if __name__ == "__main__":
    with req.urlopen('https://intranet.hbtn.io/status') as res:
        html = res.read()
        print('Body Response:')
        print("    - type: {}".format(type(html)))
        print('    - content: {}'.format(html))
        print('    - utf8 content: {}'.format(html.decode('utf-8')))
