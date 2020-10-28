from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

# driver <- 드라이버 변수. 웹 브라우저 하나에 대응된다.


# 상대경로. chromedriver를 해당 경로에 위치시켰기 때문임
"""
chromedriver 최신 버전은 http://chromedriver.chromium.org/downloads
크롬 버전이 안 맞다는 오류가 나오면 크롬 업데이트 해 주면 됨
"""
driver.get('https://www.naver.com/')
driver.implicitly_wait(10)

driver.find_element_by_id('query').send_keys('신촌 스터디룸')
# input 등 텍스트를 입력할 수 있는 HTML요소를 선택하고 send_keys() 함수를 사용하자
# 반드시 단일 HTML요소에 사용되어야 한다. 즉, find_elements_by를 사용하면 에러 발생
driver.find_element_by_css_selector('button#search_btn > span.ico_search_submit').click()

# html = driver.page_source
# driver가 위치한 현재 웹페이지의 소스 코드를 얻는 기능
# 정적 수집의 soup = BeautifulSoup(html,'html.parser')와 같이 raw html를 획득하는 코드와 같다.

info = driver.find_elements_by_css_selector('dl.info_area')

for eachinfo in info:
    name = eachinfo.find_element_by_tag_name('dt > a').text
    print(name)



# 정적 수집과 동일하게 뽑을 수도 있다.

from bs4 import BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

info_list = soup.select('dl.info_area')
for eachinfo in info_list:
    title = eachinfo.select_one('dt > a').text
    print(title)
