# -*- coding:utf-8 -*-
import sys
import os
import time
import urllib
import urllib2

def getHttp(url):
    http_hd = urllib.urlopen(url)
    return http_hd.read()

while True:
    try:
        http_txt = getHttp('http://abcabc.gq')
    except IOError:
        print 'get abcabc io error'
    else:
        pass

    try:
        http_txt = getHttp('http://window.gq/')
    except IOError:
        print 'get window io error'
    else:
        pass

    try:
        http_txt = getHttp('http://mytool.gq/')
    except IOError:
        print 'get mytool io error'
    else:
        pass

    localtime = time.asctime( time.localtime(time.time()) )
    print "time:", localtime
    time.sleep(60)
