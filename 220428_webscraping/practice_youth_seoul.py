from bs4 import BeautifulSoup
import requests

# url = 'https://youth.seoul.go.kr/site/main/home'
# 페이지
num = 1
# 청년지원정보
res_url = 'https://youth.seoul.go.kr/site/main/customSupp/politicsList?cp=' + str(num) + '&pageSize=5&searchIndex=1'


'''
params = {
    '' : '',
    '' : ''
}
headers = {
    '' : '',
    '' : ''
}
'''

# 요청
# res = requests.get(url, params=params, headers=headers)
# res = requests.get(res_url)
res = requests.get(res_url)

# Parsing(document 분석)
soup = BeautifulSoup(res.text)

'''
[css]               -->    [soup.select()]
class: '.'                  soup.select('.bx')
id: '#'                     soup.select('#sp_nws1')
계층관계 : '(공백)', '>'        soup.select(ul.list_news > li.bx)

'''


#ul.service-policy1
ul_tag = soup.select('ul.service-policy1')
# print(ul_tag)

import json
data1 = res.json()
data2 = json.loads()
print(data2)