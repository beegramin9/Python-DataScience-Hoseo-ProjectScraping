import requests
from bs4 import BeautifulSoup

res = requests.get('https://tv.naver.com/r')
raw = res.text
html = BeautifulSoup(raw,'html.parser')

clips1_3 = html.select('div.info')
clips4_100 = html.select('div.cds')

info = {}
for clip in clips1_3:
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

for clip in clips4_100:
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


print(info)

def sort_by_score(item):
    return item[1]['score']

print(sorted(info.items() , key = sort_by_score , reverse=True))