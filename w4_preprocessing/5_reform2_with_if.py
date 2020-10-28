import requests
from bs4 import BeautifulSoup

res = requests.get('https://tv.naver.com/r')
raw = res.text
html = BeautifulSoup(raw,'html.parser')

clips = html.select('dl.cds_info')

info_fail = {}

for clip in clips:
    chn = clip.select_one('dd.chn').text.strip()
    if chn not in info_fail.keys():
        info_fail[chn] = {'hit':0,'like':0}
    else:
        hit = int(clip.select_one('span.like').text.replace(',','')[5:])
        like = int(clip.select_one('span.hit').text.replace(',','')[6:])
        info_fail[chn]['hit'] += hit
        info_fail[chn]['like'] += like

print(info_fail)

# 이렇게 하면 채널이 두 번 나온 애들만 집계가 되고(그마저도 맨 처음 나왔을 때 좋아요, 조회수는 카운트 안됨)
# 한 번만 나온 애들은 아예 집계가 안 된다.
# 없을 때를 기준으로 해서 그렇다. 모든 애들이 첫 번째엔 없으니까 무조건 한 번씩 씹히잖아?

info_success = {}

for clip in clips:
    chn = clip.select_one('dd.chn').text.strip()
    hit = int(clip.select_one('span.like').text.replace(',','')[5:])
    like = int(clip.select_one('span.hit').text.replace(',','')[6:])
    if chn in info_success.keys():
        info_success[chn]['hit'] += hit
        info_success[chn]['like'] += like
    else:
        info_success[chn] = {'hit':hit,'like':like}

print(info_success)