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


print(info)

def sort_by_score(item):
    return item[1]['score']

print(sorted(info.items() , key = sort_by_score , reverse=True))