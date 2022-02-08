from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import configparser
import datetime
import calendar

class FlightTicket():
    def __init__(self):
        self.config= configparser.ConfigParser()
        self.config.read('/Users/kij/workspace/config.ini')
        
        chrome_options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        # self.browser = webdriver.Chrome(executable_path=r'220208/config.ini')

    def getWeekNo(self, month, day):
        year = datetime.datetime.now().date().year

        # 매월 1일이 무슨 요일인지 찾는다
        firstWeekDay = calendar.weekday(year, month, 1)
        # 일요일부터 시작해서, 첫번째 일요일이 언제인지 찾는다
        firstSunday = 7 - firstWeekDay
        # 몇번째 주인지 넘긴다. 7로 나눠서 나머지 0이면 +2로 둘째주가 된다.
        weekno = (day - firstSunday)//7 + 2

        return weekno, calendar.weekday(year, month, day)



    def setDay(self, way):
        if way == 'DEPARTURE':
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, 
                '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]'))).click()

            time.slee(2)
            
            month = int(self.config['DEPARTURE']['MONTH'])
            day = int(self.config['DEPARTURE']['DAY'])
            print(month, day)

            weekno, weekday = self.getWeekNo(month, day)
            # print(weekno, weekday)

            # 2월 10일(목)
            self.browser.find_element(By.XPATH, 
                         f'//*[@id="__next"]/div/div[1]/div[11]/div[2]/div[1]/div[2]/div/div[{month}]/table/tbody/tr[{weekno}]/td[{(weekday +2)%7}]/button')
             #  3월 10일(목) //*[@id="__next"]/div/div[1]/div[11]/div[2]/div[1]/div[2]/div/div[3      ]/table/tbody/tr[2       ]/td[5               ]/button
             #  2월 17일(목) //*[@id="__next"]/div/div[1]/div[11]/div[2]/div[1]/div[2]/div/div[2      ]/table/tbody/tr[3       ]/td[5               ]/button         

            # print(month, day)

    def reserve(self):
        self.browser.maximize_window()

        url = 'https://flight.naver.com/'
        self.browser.get(url)

        elem = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]'))).click()

        elem.click()
        time.slee(2)



if __name__ == '__main__':
    ticket = FlightTicket()
    ticket.reserve()