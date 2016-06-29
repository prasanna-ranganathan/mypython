#!/usr/bin/python

import sys
import requests

def check_for_redirects(url):
    try:
        r = requests.get(url,allow_redirects=False,timeout=0.5)
        if 300 <= r.status_code < 400:
            return r.headers['location']
        else:
            return '[no redirect]'
    except requests.exceptions.Timeout:
        return '[TimeOut]'
    except requests.exceptions.ConnectionError:
        return '[ConnectionTimeOut]'

def Check_domains(urls):
    for url in urls:
        check_url = url if url.startswith('http') else "http://%s" % url
        redirect_url = check_for_redirects(check_url)
        print("%s==>%s" % (check_url,redirect_url))

if __name__ == '__main__':
    try:
        fname = sys.argv[1]
    except IndexError:
        pass
    urls = ( url.strip() for url in open(fname).readlines() )
    Check_domains(urls)


