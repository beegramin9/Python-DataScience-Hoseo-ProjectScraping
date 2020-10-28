# 네이버 tv 1~3위까지 영상의 정보 가져오기 

import requests
from bs4 import BeautifulSoup

res = requests.get('http://tv.naver.com/r/')
raw = res.text
html = BeautifulSoup(raw,'html.parser')
 
top3 = html.select('div.info')

for clip in top3:
    title = clip.select_one('strong.tit > span').text
    chn = clip.select_one('dd.chn a').text
    hit = clip.select_one('span.hit').text
    like = clip.select_one('span.like').text
    print(title,'/',chn,'/',hit,'/',like)
