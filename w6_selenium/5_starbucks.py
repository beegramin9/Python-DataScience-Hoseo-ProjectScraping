# https://brunch.co.kr/@jk-lab/18
from bs4 import BeautifulSoup
import requests

url = 'https://www.istarbucks.co.kr/store/store_map.do'
'''
res = requests.get(url)
raw = res.text
html = BeautifulSoup(raw,'html.parser')

cafes = html.select('li.quickResultLstCon')

for cafe in cafes:
    print(cafe.select_one('strong').text)
'''

# 아무것도 나오지 않는다!
# 해당 크롤러가 가져온 것은 우리가 매장 찾기 -> 지역 검색 -> 서울 -> 전체
# 를 통해서 가져온 정보이다.

# 그러나 url을 살펴보면 기본 페이지와 사용자가 검색했을 때 나오는 페이지의 url이 같다.
# 따라서 현재 크롤러에게는 li.quickResultLstCon이 존재하지 않는 것

from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
'''
오류: selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element
버튼이 눌러지기 전에 함수가 실행된다는 말임. 그래서 버튼을 찾을 수가 없는거임
해결책은 driver 밑에 driver.implicitly_wait(20)
'''
import time
# driver.maximize_window()  윈도우 최대화면
driver.get(url)
# driver.implicitly_wait(20) # 20초 정도 기다리게 함
time.sleep(3)

javaclick = driver.find_element_by_css_selector('.loca_search a')
driver.execute_script('arguments[0].click();',javaclick)
time.sleep(3)

seoul = driver.find_element_by_xpath('//a[text() = "서울"]')
driver.execute_script('arguments[0].click();',seoul)
time.sleep(3)

spots = driver.find_element_by_class_name('gugun_arae_box')
spots_all = spots.find_element_by_tag_name('li')
driver.execute_script('arguments[0].click();',spots)
time.sleep(3)
# 왜 전체가 클릭이 안 되는거죠...?

raw = driver.page_source # requests 정적 수집의 raw와 같음.
html = BeautifulSoup(raw,'html.parser')
cafes = html.select('li.quickResultLstCon')

for cafe in cafes:
    print(cafe.select_one('strong').text)