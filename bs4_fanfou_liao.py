# from bs4 import BeautifulSoup

import urllib
import urllib2

url = 'http://www.fanfou.com'
query = {"loginname": "liaoleejun@163.com",
         "loginpass": "wikijun123",
         "action": "login",
         "token": "12345678"
         }
data = urllib.urlencode(query)

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
           'Referer':'http://www.fanfou.com/'}

request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)

print response.read()
