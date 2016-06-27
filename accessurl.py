# -*- coding:utf-8 -*-
import sys
import os
import time
import urllib
import urllib2

def getHttp(url):
    http_hd = urllib.urlopen(url)
    return http_hd.read()


http_txt = getHttp('http://abcabc.gq')
print http_txt
http_txt = getHttp('http://window.gq/')
print http_txt
http_txt = getHttp('http://mytool.gq/')
print http_txt
