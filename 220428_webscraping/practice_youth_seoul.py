from bs4 import BeautifulSoup
import requests

# url = 'https://youth.seoul.go.kr/site/main/home'
# 페이지
num = 1
# 청년지원정보
res_url = 'https://youth.seoul.go.kr/site/main/customSupp/politicsList?cp=' + str(num) #+ '&pageSize=5&searchIndex=1'


params = {
    'pageSize' : '5',
    'searchIndex' : '1'
}
'''
headers = {
    '' : '',
    '' : ''
}
'''

# 요청
# res = requests.get(url, params=params, headers=headers)
# res = requests.get(res_url)
res = requests.get(res_url, params=params)

# Parsing(document 분석)
soup = BeautifulSoup(res.text)

'''
[css]               -->    [soup.select()]
class: '.'                  soup.select('.bx')
id: '#'                     soup.select('#sp_nws1')
계층관계 : '(공백)', '>'        soup.select(ul.list_news > li.bx)

'''


#ul.service-policy1
ul_tag = soup.select('ul.service-policy1 a')
# print(ul_tag)


result_list = []
for a in ul_tag:
    a_tag_dict = {
        # '링크': a.select_one('').get('href'),
        # '제목': a.select_one('').text,
        '상태': a.select_one('span.ml_5').text
    }
    result_list.append(a_tag_dict)

# print(result_list)

string1 = str(ul_tag[0]).split('>')

# print(string1)
# print(string1[1])

import json
# data1 = res.json()
# data2 = json.loads()
# print(data2)

p_url = 'https://youth.seoul.go.kr/site/main/youth/politics/user/detail/16361'

resp = requests.get(p_url)
soup = BeautifulSoup(resp.text)
# data3 = resp.json()
# data3 = json.loads()
# print(data3)


# print(soup.select('.se-text-paragraph se-text-paragraph-align-center '))


b_url = 'https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do'

# 페이지
num = 1

params = {
    'pageIndex': str(num),
    'trgtJynEmp' : '',
    'trgtJynEmp' : ''
}

res_p = requests.get(b_url, params=params)
soup = BeautifulSoup(res_p.text)
print(res_p.text)