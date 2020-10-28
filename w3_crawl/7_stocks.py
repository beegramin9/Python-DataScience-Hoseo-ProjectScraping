import requests
from bs4 import BeautifulSoup

raw = requests.get('https://finance.naver.com/sise/lastsearch2.nhn').text
html = BeautifulSoup(raw,'html.parser')

stocks = html.select('a.tltle')
# 홈페이지 상에서 오타가 존재하는 경우
for stock in stocks:
    print(stock.text)