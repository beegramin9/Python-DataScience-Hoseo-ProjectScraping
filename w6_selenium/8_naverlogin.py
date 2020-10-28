from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('http://naver.com')
driver.implicitly_wait(1)

xpath = '//*[@id="account"]/a'
driver.find_element_by_xpath(xpath).click()

id_login = driver.find_element_by_id('id')
id_login.clear()
pyperclip.copy('spald1ng')
id_login.send_keys(Keys.CONTROL, 'v')
driver.implicitly_wait(1)


id_login = driver.find_element_by_id('pw')
id_login.clear()
pyperclip.copy('wtchoe13')
id_login.send_keys(Keys.CONTROL, 'v')
driver.implicitly_wait(1)

driver.find_element_by_id('log.login').click()

driver.get('https://mail.naver.com')
driver.implicitly_wait(2)


raw = driver.page_source
# Selenium이 접근한 소스를 그대로 넘겨 받습니다.

html = BeautifulSoup(raw, "html.parser")

senders = html.select('div.mTitle a')
print(senders)
