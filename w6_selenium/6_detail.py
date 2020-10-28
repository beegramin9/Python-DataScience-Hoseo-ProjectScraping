from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
driver.get('https://map.kakao.com/')
driver.implicitly_wait(10)

import time
search = driver.find_element_by_id('search\.keyword\.query').send_keys('신촌 스터디룸')
time.sleep(1)

button = driver.find_element_by_id('search\.keyword\.submit').send_keys('\n')
time.sleep(1)

more = driver.find_element_by_xpath('//a[text()="장소 더보기"]')
driver.execute_script('arguments[0].click();',more)
time.sleep(1)


pagewrap = driver.find_element_by_id('info\.search\.page')
time.sleep(1)

page = 1

while True:
    page += 1
    try:
        index = pagewrap.find_element_by_xpath('//a[text()='+str(page)+']')
        driver.execute_script('arguments[0].click();',index)
        # 왜 2까지밖에 페이지가 안 넘어가지...?
        time.sleep(1)
        details = driver.find_element_by_css_selector('div.contact clickArea')
        for detail in details:
            moreview = detail.find_element_by_css_selector('a.moreview')
            # Selenium에서도 꼬리물듯이 css선택 가능
            moreview.send_keys('\n')
            time.sleep(1)
            driver.switch_to_window(driver.window_handles[1])
            # 조종 중인 브라우저의 탭을 바꿀 수 있음
            time.sleep(1)
            driver.close()
            # 탭 닫기
            time.sleep(1)
            driver.switch_to_window(driver.window_handles[0])
            # 본래 홈페이지로 돌아가기
            time.sleep(1)
    except:
        break



