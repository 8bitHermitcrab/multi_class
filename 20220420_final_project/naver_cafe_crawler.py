import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import json

json.dumps({"query":"=취미생활추천","page":2,"sortBy":0,"period":["20211201","20220228"]})

n_cafe_list2 = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/Users/kimberlyjojohirn/Downloads/chromedriver', chrome_options=chrome_options)
# 여가, 문화, 취미, 트렌드, 여행
for num in range(2, 3): # 1페이지부터 10페이지까지
  # url = 'https://section.cafe.naver.com/ca-fe/home/search/articles?q==%EC%B7%A8%EB%AF%B8%EC%83%9D%ED%99%9C%EC%B6%94%EC%B2%9C&p=2&pr=7&ps=2021.12.01&pe=2022.02.28'
  # req = urllib.request.Request(url)
  # source_code = urllib.request.urlopen(url).read()

  ref_url = 'https://section.cafe.naver.com/ca-fe/home/search/articles?q==%EC%B7%A8%EB%AF%B8%EC%83%9D%ED%99%9C%EC%B6%94%EC%B2%9C&p=2&pr=7&ps=2021.12.01&pe=2022.02.28'
  url = 'https://apis.naver.com/cafe-home-web/cafe-home/v1/search/articles'

  driver.get(url)
  source_code = driver.page_source
  soup = bs(source_code, 'html.parser')
  
#   for n in soup.find_all('p', 'item_content'):
#     n_cafe_list2.append(n.get_text())

# print(n_cafe_list2)


data = {"query":"=취미생활추천","page":2,"sortBy":0,"period":["20211201","20220228"]}
sess = requests.session()
s = sess.get(ref_url)
resp = requests.post(url, json=data)

print(resp.text)