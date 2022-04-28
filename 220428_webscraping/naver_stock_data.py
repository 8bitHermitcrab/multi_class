import requests
from bs4 import BeautifulSoup

result_list = []

# url 찾기
url = 'https://finance.naver.com/item/sise.nhn'

params = {
    'code' : '005930' # 삼성전자
}

# 요청
resq = requests.get(url, params=params)

# Parsing(document 분석)
soup = BeautifulSoup(resq.text)

table_tags = soup.select('table')
print(len(table_tags))

headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

# iframe
resp = requests.get('https://finance.naver.com/item/sise_day.naver', params={
    'code' : '005930'   
}, headers=headers)
soup = BeautifulSoup(resp.text)
print(soup)