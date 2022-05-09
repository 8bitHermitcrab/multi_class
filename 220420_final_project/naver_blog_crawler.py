# 네이버 블로그 크롤러

import pandas as pd
from selenium import webdriver
import datetime
import time
import requests
from bs4 import BeautifulSoup as bs
import urllib.parse
from selenium.webdriver.common.keys import Keys

blog_list2 = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

def click_nolink_for_scrollDown(driver, scrollDown_num=50000):
  url = 'https://search.naver.com/search.naver?where=post&query='
  k = '여가'
  num = 1
  url = url + urllib.parse.quote(k) + '&sm=tab_opt&date_option=4&start=' + str(num)
  req = urllib.request.Request(url)
  source_code = urllib.request.urlopen(url).read()
  soup = bs(source_code, 'html.parser')

  time.sleep(0.1)
  for i in range(scrollDown_num):
    time.sleep(0.1)
    body = driver.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN)

  for n in soup.find_all('div', 'api_txt_lines dsc_txt'):
    blog_list2.append(n.get_text())

print(click_nolink_for_scrollDown(driver))

print(len(blog_list2))

print(blog_list2[:3])