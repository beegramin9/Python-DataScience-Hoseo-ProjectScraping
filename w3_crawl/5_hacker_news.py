import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/news?p='

# select로 리스트 형태로 받은 후 리스트 내부를 문자열로
for page in range(1):
    res = requests.get(url,str(page+1), headers={'User-Agent':'Mozilla/5.0'})
    raw = res.text
    html = BeautifulSoup(raw,'html.parser')

    titles = html.select('a.storylink')
    output = []
    for title in titles:
        title = title.text
        output.append(title)
        for element in output:
            print(element)
