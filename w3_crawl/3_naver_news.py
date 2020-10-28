# 네이버 뉴스 검색 수집

import requests
from bs4 import BeautifulSoup

res = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%95%84%EC%8B%9C%EC%95%88%EA%B2%8C%EC%9E%84',
headers = {'User-Agent':'Mozilla/5.0'})
raw = res.text
html = BeautifulSoup(raw,'html.parser')

# 한 기사 전체를 커버하는 html주소를 찾는게 좋다.
# 나중에 언론사, 요약 내용, 연관 뉴스 등을 검색할 수도 있기 때문이다.

articles = html.select('ul.type01 > li')
# ul.type01 까지만 하면 왜 하나만 나오고
# 자손선택자를 써줘야지만 li가 나오는 걸까?

for article in articles:
    journal = article.select_one('span._sp_each_source').text
    title = article.select_one('a._sp_each_title').text
        
    print(journal,'/',title)

