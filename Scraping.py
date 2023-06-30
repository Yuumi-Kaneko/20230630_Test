import requests
from bs4 import BeautifulSoup

res = requests.get('https://lis.inf.kyushu-u.ac.jp/')
soup = BeautifulSoup(res.text,'https://lis.inf.kyushu-u.ac.jp/')
text = soup.h2.string

print(text)

##Couldn't find a tree builder with the features you requested: https://lis.inf.kyushu-u.ac.jp/. Do you need to install a parser library?
##上のエラーで終了