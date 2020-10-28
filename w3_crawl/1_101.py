# 클래스: 속성과 그 속성에 적용되는 메소드들을 미리 묶어놓은 집합체 
import requests
from bs4 import BeautifulSoup

res = requests.get('http://tv.naver.com/r/')
# requests 모듈의 response 클래스  
raw = res.text
# response 타입 함수 중 하나인 .text 함수를 통하여 문자열로 변환 가능
# 이때부터 strip()/.replace() 와 같은 문자열 타입 함수 사용 가능

html = BeautifulSoup(raw,'html.parser')
# BeautifulSoup을 거쳐야만 bs4.BeautifulSoup 클래스.
# 단, 이 경우에는 문자열 타입 함수를 사용하지 못함, 왜? 얘는 이미 html임
# .select/.select_one/.text 와 같은 bs4 타입 함수 사용 가능

units = html.select('div.cds')
# select 함수는 여러 요소가 존재할 경우를 대비하여 항상 리스트로 결과를 돌려줌
# 결과가 하나라도 원소개수가 하나인 리스트로 나온다.
# 따라서 하나일 때에는 select_one을 사용하면 된다.

#  첫 번째 영상의 정보만 가져오기
clip1 = units[0]
clip1_title = clip1.select_one('dt.title tooltip')
clip1_channel = clip1.select_one('dd.chn > a')
clip1_hit = clip1.select_one('span.hit')
clip1_like = clip1.select_one('span.like')

print(clip1_title)
print(clip1_channel)
print(clip1_hit)
print(clip1_like)

#  4~100위까지 영상의 정보 가져오기
for clip in units:
    title = clip.select_one('dt.title tooltip').text
    channel = clip.select_one('dd.chn > a').text
    hit = clip.select_one('span.hit').text
    like = clip.select_one('span.like').text
    print(title,channel,hit,like)
#