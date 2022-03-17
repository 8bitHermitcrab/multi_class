# 크롬 브라우저를 제어하기 위해 webdriver를 임포트
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome(executable_path=r'/Users/kij/workspace/220208/chromedriver.exe')
browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get('http://naver.com')

# browser.find_element_by_class_name('link_login').click()
""" 
# 뒤로가기
browser.back()
# 앞으로 가기
browser.forward()
# 새로고침
browser.refresh() 
"""

# 브라우저 검색창에 자동으로 문자 검색해보기
# query = browser.find_element_by_id('query')
# query.send_keys('멀티캠퍼스')
# query.send_keys(Keys.ENTER)

# tag = browser.find_element_by_tag_name('a')
# print(tag)

# tags = browser.find_elements_by_tag_name('a')
# for tag in tags:
#     print(tag.get_attribute('href'))

browser.get('http://daum.net')

query = browser.find_element_by_name('q')
query.send_keys('멀티캠퍼스')
# query.send_keys(Keys.ENTER)

browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]').click()

browser.quit()