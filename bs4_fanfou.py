import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup

filename = 'cookie.txt'
fanfou = 'http://fanfou.com/'
cj = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.open(fanfou)
postdata = urllib.urlencode({
    'loginname': 'liaoleejun@163.com',
    'loginpass': 'wikijun123',
    'action': 'login',
    'token': '12345678'
})
req = urllib2.Request('http://fanfou.com/login', postdata)
result = opener.open(req)
res = '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> '
for i in range(1, 119):
    pageURL = 'http://fanfou.com/~RLhcIDBjZAM/p.' + str(i)
    result = opener.open(pageURL)
    content = result.read()
    soup = BeautifulSoup(content)
    content = soup.find_all("span", class_="content")
    for elem in content:
        res = res + str(elem)+'<br><br>'
    res += '<br><br><br>'
    print i

fp = open("fanfou.html", "w")
fp.write(res)
fp.close()
