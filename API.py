import requests

res = requests.get('https://zipcloud.ibsnet.co.jp/api/search?zipcode=1000001')
print(res.status_code)
print(res.text)