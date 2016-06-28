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
    log=''
    log += time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
    log += "\r\n"
    try:
        http_txt = getHttp("http://abcabc.gq")
    except IOError:
        log += "get abcabc io error\r\n"
    else:
        pass

    try:
        http_txt = getHttp("http://window.gq/")
    except IOError:
        log += "get window io error\r\n"
    else:
        pass

    try:
        http_txt = getHttp("http://mytool.gq/")
    except IOError:
        log += "get mytool io error\r\n"
    else:
        pass

    logfile = open("/var/vol/text.txt", 'a')
    try:
        #print log
        logfile.write(log)
    finally:
        logfile.close()
    time.sleep(60)
