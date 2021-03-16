#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def finddeadlinks(url, depth, pre=' ', count=0):
    temp = count
    try:
        resp = requests.head(url)
        if 400 <= int(resp.status_code) < 600:
            deadlinks.append(url)
            print(pre, ": ", url)
        else:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            for a in soup.find_all('a', href=True):
                count = temp
                if a['href'].startswith('http'):
                    if depth != count:
                        count += 1
                        finddeadlinks(a['href'], depth, url, count)
                else:
                    if depth != count:
                        count += 1
                        finddeadlinks(url+a['href'], depth, url, count)
    except:
        print(pre, ": ", url)

if __name__ == '__main__':
    from pathlib import Path
    from sys import argv


    if len(argv) not in [2,3]:
        print('not enough')
        exit(1)
    if argv[1].startswith('-'):
        try:
            depth = int(argv[1][1:])
            url = argv[2]
        except ValueError:
            print("invalid number")
            exit(1)
        if len(argv) == 2:
            print("No URL")
            exit(1)
    else:
        if len(argv) == 2:
            depth = 0
            url = argv[1]
        else:
            print('invalid input')
            exit(1)

    depth += 1
    finddeadlinks(url, depth)
   
