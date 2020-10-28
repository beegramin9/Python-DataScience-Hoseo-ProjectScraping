import datetime
dt = datetime.datetime.now()
print(dt)
'''
2020-02-09 23:58:28 이런 식으로 나오는데
이를 그대로 파일명으로 쓰기엔 부적절함
날짜까지만 필요하고 무엇보다도 파일명에는 :가 올 수 없음
'''

df = dt.strftime('%Y_%m_%d')
print(df)
# string formatted(형식화된) time
'''
%H, %M, %S 시간, 분, 초
'''

filename = '3_datetime_Top100_'+df

f = open(filename,'w')

import requests
from bs4 import BeautifulSoup

res = requests.get('https://tv.naver.com/r')
raw = res.text
html = BeautifulSoup(raw,'html.parser')

clips = html.select('dl.cds_info')

info = {}

for clip in clips:
    chn = clip.select_one('dd.chn').text.strip()
    hit = int(clip.select_one('span.like').text.replace(',','')[5:])
    like = int(clip.select_one('span.hit').text.replace(',','')[6:])
    score = hit + like*350/100
    if chn in info.keys():
        info[chn]['hit'] += hit
        info[chn]['like'] += like
        info[chn]['score'] += score
    else:
        info[chn] = {'hit':hit,'like':like,'score':score}

def sort_by_score(item):
    return item[1]['score']

for arg in sorted(info.items() , key = sort_by_score , reverse=True):
    f.write(arg[0]+
        str(arg[1]['hit'])+','+str(arg[1]['like'])+','+str(arg[1]['score'])+'\n')

f.close()