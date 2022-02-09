from selenium import webdriver
from time import sleep
import sys


print(sys.argv[1].split('|,'))



class GrammarlyBot():
    def __init__(self,comment):
        self.driver = webdriver.Chrome()
        self.comment=comment

    def login(self):
        self.driver.get('https://app.grammarly.com/ddocs/594240786')
        sleep(10)
        login= self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div/div[2]/nav[2]/ul/li/a')
        login.click()
        sleep(5)
        email = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/div/input')
        email.send_keys('your email')
        continue_btn = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div/div[2]/div/div/button')
        continue_btn.click()
        sleep(2)
        password = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/input')
        password.send_keys('your password')
        sigin=self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div/div[2]/div/div/button')
        sigin.click()
        sleep(10)
        demo=self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div[2]/div[4]/div/div[3]/div[2]/div[3]/a')
        demo.click()

    def correct(self):
        send_comment = self.driver.find_element_by_xpath('//*[@id="page"]/div/div[2]/div[2]/div/div[4]/div[3]/div[1]/div[1]/div/div/div[10]/div[1]')
        send_comment.send_keys(self.comment)
        sleep(10)
        all_suggestions=self.driver.find_element_by_xpath('//*[@id="page"]/div/div[2]/div[2]/div/div[4]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div')
        all_suggestions.click()

        #check with css selector if an element do exists
        exist=self.driver.find_elements_by_css_selector('body > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(1) > text:nth-child(2)')
        while exist:
          small_win=self.driver.find_element_by_xpath('//*[@id="page"]/div/div[2]/div[2]/div/div[4]/div[3]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div')
          small_win.click()
          sleep(5)
          the_one= self.driver.find_element_by_xpath('//*[@id="page"]/div/div[2]/div[2]/div/div[4]/div[3]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div[2]/div')
          the_one.click()
          sleep(10)
          exist=self.driver.find_elements_by_css_selector('body > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(1) > text:nth-child(2)')

        corrected_comment= self.driver.find_element_by_xpath('//*[@id="page"]/div/div[2]/div[2]/div/div[4]/div[3]/div[1]/div[1]/div/div/div[10]/div[1]/p')
        corrected_comment=corrected_comment.text
        send_comment = self.driver.find_element_by_xpath('//*[@id="page"]/div/div[2]/div[2]/div/div[4]/div[3]/div[1]/div[1]/div/div/div[10]/div[1]')
        send_comment.clear()
        return corrected_comment

# grammarly= GrammarlyBot(sys.argv[1])
# grammarly.login()
# sleep(5)




