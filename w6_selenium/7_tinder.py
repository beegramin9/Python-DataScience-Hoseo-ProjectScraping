from selenium import webdriver
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        # 물론 함수 내부에 변수를 정해주거나 
        # 이 경우에는 다 똑같은데 앞에 self. 만 붙여주면 됨
        # 객체(주어)가 하는 행동
        self.driver.implicitly_wait(10)
        self.driver.get('http://tinder.com')

    def login(self):
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button/span[2]')
        fb_btn.click()
        
        base_window = self.driver.window_handles[0]
        # 로그인 창으로 스위치
        popup = self.driver.switch_to.window(self.driver.window_handles[1])
        
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('hapt135@hanmail.net')
        
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys('wtchoe13')
        
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        
        self.driver.switch_to.window(base_window)
        # 팝업창을 제대로 선택하기 위해 기존 윈도우로 돌아감
        popup_1 = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        
        popup_2 = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
    
    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()
    
    def auto_swipe(self):
        from random import random
        left_count, right_count = 0, 0
        while True:
            sleep(1)
            try: 
                rand = random()
                if rand < .89:
                    self.like()
                    right_count += 1
                    print('{}th right swipe'.format(right_count))    
                else:
                    self.dislike()
                    left_count += 1    
                    print('{}th left swipe'.format(left_count))    
            except Exception:
                try:
                    self.close_popup()
                except:
                    break

    def close_popup(self):
        not_interested = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        not_interested.click() 
    
    def message_all(self):
        while True:
            matches = self.driver.find_element_by_class_name('matchListItem')
            if len(matches) < 2:
                break
            matches[0].click()
            sleep(0.2)
            msg_box = self.driver.find_element_by_id('chat-text-area')
            msg_box.send_keys('Hi there')
            send_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
            send_btn.click()
            matches_tab = self.driver.find_element_by_xpath('//*[@id="match-tab"]')
            matches_tab.click()
            sleep(0.5) 


bot = TinderBot()
bot.login()
bot.auto_swipe()
bot.close_popup()