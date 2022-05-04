from bs4 import BeautifulSoup
import requests
import json

# url = 'https://youth.seoul.go.kr/site/main/home'
# 페이지
num = 1
# 청년지원정보
res_url = 'https://youth.seoul.go.kr/site/main/customSupp/politicsList?cp=' + str(num) #+ '&pageSize=5&searchIndex=1'

'''
params = {
    'pageSize' : '5',
    'searchIndex' : '1'
}
'''
'''
headers = {
    '' : '',
    '' : ''
}
'''

# 요청
# res = requests.get(url, params=params, headers=headers)
# res = requests.get(res_url)
# res = requests.get(res_url, params=params)

# Parsing(document 분석)
# soup = BeautifulSoup(res.text)

'''
[css]               -->    [soup.select()]
class: '.'                  soup.select('.bx')
id: '#'                     soup.select('#sp_nws1')
계층관계 : '(공백)', '>'        soup.select(ul.list_news > li.bx)

'''


#ul.service-policy1
# ul_tag = soup.select('ul.service-policy1 a')
# print(ul_tag)


# result_list = []
# for a in ul_tag:
#     a_tag_dict = {
#         # '링크': a.select_one('').get('href'),
#         # '제목': a.select_one('').text,
#         '상태': a.select_one('span.ml_5').text
#     }
#     result_list.append(a_tag_dict)

# print(result_list)

# string1 = str(ul_tag[0]).split('>')

# print(string1)
# print(string1[1])

# data1 = res.json()
# data2 = json.loads()
# print(data2)

# p_url = 'https://youth.seoul.go.kr/site/main/youth/politics/user/detail/16361'

# resp = requests.get(p_url)
# soup = BeautifulSoup(resp.text)
# data3 = resp.json()
# data3 = json.loads()
# print(data3)


# print(soup.select('.se-text-paragraph se-text-paragraph-align-center '))


# b_url = 'https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do'

# # 페이지
# num = 1

# params = {
#     'pageIndex': str(num),
#     'trgtJynEmp' : '',
#     'trgtJynEmp' : ''
# }

# res_p = requests.get(b_url, params=params)
# soup = BeautifulSoup(res_p.text)
# print(res_p.text)



detail_url = 'https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifDtl.do'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'youngPlcyUnifR2022011101102=youngPlcyUnifR2022011101102; WMONID=NqgOYGZzjsO; PCID=16514152408841898264996; RC_RESOLUTION=1920*1080; RC_COLOR=24; YOUTHCENTERSESSIONID=EDCKbSrUAylVxDwYAILh4O7bkXmTpbddPJuwt_RXJAH_wmfEttWJ!188653571!407080285',
    'Host': 'www.youthcenter.go.kr',
    'Origin': 'https://www.youthcenter.go.kr',
    'Referer': 'https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do',
    'Server': 'none',
    'Transfer-Encoding': 'chunked',
    'Pragma': 'no-cache',
    'X-Content-Type-Options': 'nosniff',
    'X-XSS-Protection': '1; mode=block',
    'Content-Type': 'text/html;charset=utf-8',
    'Date': 'Tue, 03 May 2022 15:21:20 GMT',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    
'''
{'Server': 'nginx', 
'Date': 'Wed, 27 Apr 2022 08:40:27 GMT',
 'Content-Type': 'application/json;charset=UTF-8',
  'Transfer-Encoding': 'chunked',
   'Connection': 'keep-alive',
    'Keep-Alive': 'timeout=5',
     'Vary': 'Accept-Encoding',
      'apigw-uuid': 'e1edc791-439f-4f4c-9bf2-42e8c6f26ae9',
       'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
         'Access-Control-Allow-Headers': 'X-Requested-With,Content-Type,charset,X-Request-From,X-Cafe-Product,X-Cafe-Version,X-Cafe-Phase',
          'Access-Control-Max-Age': '600',
           'Cache-Control': 'no-cache, no-store, max-age=0, must-revalidate',
            'Pragma': 'no-cache',
             'Expires': '0',
              'X-XSS-Protection': '1; mode=block',
               'X-Frame-Options': 'DENY',
                'X-Content-Type-Options': 'nosniff',
                 'Referrer-Policy': 'unsafe-url',
 'Content-Encoding': 'gzip'}'''

# sess = requests.session()
detail_p = requests.get(detail_url, headers=headers)
soup = BeautifulSoup(detail_p.text)
print(detail_p.text)