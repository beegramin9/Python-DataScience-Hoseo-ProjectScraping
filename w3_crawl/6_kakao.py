import requests
from bs4 import BeautifulSoup

res = requests.get('https://tech.kakao.com',headers = {'User-Agent':'Mozilla/5.0'})
# 인터프레터로 했을 때 여기서 에러가 발생함
# 아마 카카오에서 홈페이지에 크롤링을 막아 놓은 듯
raw = res.text
html = BeautifulSoup(raw,'html.parser')

tags = html.select('div.info_tag > span.txt_tag')

for tag in tags:
    print(tag)