# TV 100을 채널별로 정리하고 총 좋아요와 조회수를 구하자
# 클립별로 나열된 리스트는 순위대로 수집되기 때문에
# 슌서대로 있기만 해도 충분하지만
# 채널처럼 특정한 하나의 데이터 위주로 정리할 때는 딕셔너리
# 채널이름을 key로 하여 총 좋아요와 조회수를 값으로 갖는 딕셔너리
# https://book.coalastudy.com/data-crawling/week-4/stage-2

import requests
from bs4 import BeautifulSoup

res = requests.get('https://tv.naver.com/r')
raw = res.text
html = BeautifulSoup(raw, 'html.parser')

clips = html.select('dl.cds_info')

info = {}

for clip in clips:
    chn = clip.select_one('dd.chn').text.strip()
    info[chn] = {'hit': 0, 'like': 0}

for clip in clips:
    chn = clip.select_one('dd.chn').text.strip()
    hit = int(clip.select_one('span.like').text.replace(',', '')[5:])
    like = int(clip.select_one('span.hit').text.replace(',', '')[6:])

    info[chn]['hit'] += hit
    info[chn]['like'] += like

print(len(clips))