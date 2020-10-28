from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')

driver.get('https://papago.naver.com/')

driver.implicitly_wait(20)
search = driver.find_element_by_css_selector('#txtSource')
search.clear() # 검색창에 default로 내용이 있는 경우가 있어서 지워주는 것
search.send_keys('I love Coala study')


# SelectorGadget 이 직빵임
driver.find_element_by_id('btnTranslate').click()

# Selenium에서 Click이 되지 않을 때
# http://blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221430636045&categoryNo=35&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
"""
클릭하면 다른 화면으로 넘어가는 element를 선택하고 명령을 내렸음에도 불구하고 클릭이 되지 않을 때
Ex) <a href = 'http://test.test'> 테스트1 </a>
이 같이 a의 href 속성값에 링크가 바로 나와있을 때에는
driver.find_element_by_css_select('a').click()으로 바로 링크 접속 가능
"""
# 그러나 링크가 아닌 자바스크립트, 즉 다른 명령어가 들어가 있다면
'''
<a href = '#', onclick = 기타 명령어> 테스트2 </a>
제대로 선택을 해도 href에 url 주소가 들어가 있지 않기 때문에 해당 주소로 들어갈 수 없음
'''
# 이 경우에는 onclick 내부의 명령어가 실행되도록 해야 함
'''
첫 번째:
driver.find_element_by_css_select('a').send_keys('\n')
두 번째:
sample = driver.find_element_by_css_select('a')
driver.execute_script('argument[0].click();',sample) # 자바 명령어 실행
'''