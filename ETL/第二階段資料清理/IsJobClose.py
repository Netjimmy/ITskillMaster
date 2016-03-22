# coding=utf-8

import requests
from bs4 import BeautifulSoup as bs
import re
import time

def is518jobclose(x):
    try:
        res = requests.get(x)
        res.encoding = "UTF-8"
        soup = bs(res.text, "html.parser")
        return len(soup.select('p.job_be_close')) > 0
        time.sleep(15)
    except Exception as e:
        print "Unknown exception!" + '\n' + "Error message is %s" % e

def is104jobclose(x):
    try:
        res = requests.get(x)
        res.encoding = "UTF-8"
        soup = bs(res.text, "html.parser")
        return len(soup.select('div.wrap.closed')) > 0
    except Exception as e:
        print "Unknown exception!" + '\n' + "Error message is %s" % e

def is1111jobclose(x):
    try:
        res = requests.get(x)
        res.encoding = "UTF-8"
        soup = bs(res.text, "html.parser")
        return len(soup.select('.WRAPPER')) > 0
    except Exception as e:
        print "Unknown exception!" + '\n' + "Error message is %s" % e

def is178jobclose(x):
    try:
        res = requests.get(x)
        res.encoding = "UTF-8"
        soup = bs(res.text, "html.parser")
        return u'職缺已關閉' in soup.select('ul.path li')[0].text
    except Exception as e:
        print "Unknown exception!" + '\n' + "Error message is %s" % e

def isMitJobsjobclose(x):
    res = requests.get(x)
    res.encoding = "UTF-8"
    soup = bs(res.text, "html.parser")
    return "The page you were looking for doesn't exist" in soup.select('title')[0].text

def isYes123jobclose(x):
    try:
        res = requests.get(x)
        res.encoding = "UTF-8"
        soup = bs(res.text, "html.parser")
        r = soup.select('#container tr td')[0].text
        if re.search(u"該企業已關閉此職缺，請您重新查詢", r):
            return 'True'
        else:
            return 'False'
    except Exception as e:
        print "Unknown exception!" + '\n' + "Error message is %s" % e

# ---------------------------------------------------------------------------------------------------------------------

def isJobClose(x):

    if re.search('www.yes123.com.tw', x):
        return isYes123jobclose(x)
    if re.search('www.518.com.tw', x):
        return is518jobclose(x)
    if re.search('mit.jobs', x):
        return isMitJobsjobclose(x)
    if re.search('www.job178.com.tw', x):
        return is178jobclose(x)
    if re.search('www.1111.com.tw', x):
        return is1111jobclose(x)
    if re.search('www.104.com.tw', x):
        return is104jobclose(x)

    return 'ERROR'

# ---------------------------------------------------------------------------------------------------------------------

# print isJobClose('http://www.104.com.tw/job/?jobno=5pxhr&jobsource=104_bank1&hotjob_chr=')
