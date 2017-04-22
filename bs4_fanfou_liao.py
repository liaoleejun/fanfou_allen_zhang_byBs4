# coding=utf-8

"""
参考自:
1. http://cuiqingcai.com/968.html
2. liuwei
"""

import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup

filename = 'cookie.txt'
url = 'http://www.fanfou.com'

# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
opener.open(url)
data = urllib.urlencode({
    "loginname": "liaoleejun@163.com",
    "loginpass": "wikijun123",
    "action": "login",
    "token": "12345678"
})

request = urllib2.Request('http://fanfou.com/login', data)

# 这个请求带了cookie，所以用urllib2.urlopen()方法是不行的，必须用opener.open() 方法
# response = urllib2.urlopen(request)
response = opener.open(request)

res = '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> '
for i in range(1, 119):
    pageURL = 'http://fanfou.com/~RLhcIDBjZAM/p.' + str(i)
    result = opener.open(pageURL)
    content = result.read()
    soup = BeautifulSoup(content)
    text = soup.find_all("span", class_="content")
    for elem in text:
        res = res + str(elem) + '<br><br>'
    res += '<br><br><br>'
    print i

fp = open("fanfou2.html", "w")
fp.write(res)
fp.close()
