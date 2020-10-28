from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
driver.get('https://map.kakao.com/')
driver.implicitly_wait(10)

driver.find_element_by_css_selector('#search\.keyword\.query').send_keys('카페')
driver.find_element_by_css_selector('#search\.keyword\.submit').send_keys('\n')
# a 속성이 아닌 검색창, 버튼일 때 잘 먹힘

javaclick = driver.find_element_by_css_selector('#info\.search\.place\.more')
driver.execute_script('arguments[0].click();',javaclick)
# <a href = '#', 기타 명령어> 텍스트 </a>. 즉 a href가 있긴 있는데 # 일 때 잘 먹힘

import time

page = 1 
while True:
    page += 1
    try:
        driver.find_element_by_xpath('//*[@id="info.search.page.no'+str(page)+']').click()
        time.sleep(1)
    except:
        break
