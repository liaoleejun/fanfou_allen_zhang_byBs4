# coding: utf-8

# Python 3, requests版本 (因为Python 2在2020年会退休不再维护; 同时, 大家都在推荐
# 用requests库, 而不是urllib)
# 需要: 导入requests和bs4库 (是bs4而不是BeautifulSoup)

import requests
from bs4 import BeautifulSoup

login_url = 'http://fanfou.com/login'
# payload是用Chrome监测登录的网络看到的, 其中用户名和密码是注册的
# Todo token取12345678也是可以的, 有待进一步探究
payload = {
    "loginname": "wqsaxz@wqsaxz.com",
    "loginpass": "wqsaxz",
    "action": "login",
    "token": "12345678"
}

# 参考: https://stackoverflow.com/a/17633072
with requests.Session() as s:
    s.post(login_url, data=payload)
    res = '<meta http-equiv="Content-Type" content="text/html; ' \
          'charset=utf-8" />'
    # 119是人工看到的网页总共有119页 (Todo 有待进一步优化, 来实现自动化)
    for i in range(1, 119):
        page_url = 'http://fanfou.com/~RLhcIDBjZAM/p.' + str(i)
        content = s.get(page_url).text
        # 带上第二个参数 "html.parser", 否则会报 warning
        soup = BeautifulSoup(content, "html.parser")
        text = soup.find_all("span", class_="content")
        time = soup.find_all("a", class_="time")

        for j in range(len(text)):
            res = res + str(time[j]) + ' ' + str(text[j]) + '<br><br>'
        res += '<hr>'
        print(str(i) + 'th page')

# 必须加上encoding="utf-8"这个参数, 否则会乱码。
# 大概是open函数默认调用系统的字符编码gbk
fp = open("fanfou.html", "w", encoding="utf-8")
fp.write(res)
fp.close()
