import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%95%84%EC%8B%9C%EC%95%88%EA%B2%8C%EC%9E%84&oquery=%EC%95%84%EC%8B%9C%EC%95%88%EA%B2%8C%EC%9E%84&tqi=UBI5Fwp0J1sssdlGSCGssssstRZ-482102&start='

for start in range(3):
    res = requests.get(url,
                       str(start * 10 + 1),
                       headers={'User-Agent': 'Mozilla/5.0'})
    # 문자열과 숫자는 같이 합쳐질 수 없으므로 str을 통해서 숫자를 문자열로
    raw = res.text
    html = BeautifulSoup(raw, 'html.parser')
    articles = html.select('ul.type01 > li')

    for article in articles:
        journal = article.select_one('span._sp_each_source').text
        title = article.select_one('a._sp_each_title').text

        print(journal, '/', title)

# for i in range(3):
#     페이지마다 할 일들...
#
#     for article in articles:
#         페이지 내의 기사마다 할 일들...
#
#         print('페이지', i, '완료')