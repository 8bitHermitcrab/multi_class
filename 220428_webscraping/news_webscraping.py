from bs4 import BeautifulSoup
import requests


# 네이버 뉴스 크롤링
# 네이버 뉴스 "무역전쟁"을 3페이지, 다음과 같은 형태로 저장.
# [{
#   'url' : 'http://...',
#   'title' : '',
#   'desc' : '',
#   'contents' : '', # 상세페이지 html
#   'thumbnail' : '' # 뉴스 목록에 잇는 이미지 없을시 None
# }]


# 1. url 파악
url = 'https://search.naver.com/search.naver'
params = {
    'where' : 'news',
    'query' : '무역전쟁'
}

# 2. 검색결과 url에 요청 보내기
resp = requests.get(url, params=params)
print(resp)

# 3. BeautifulSoup으로 parsing 하고 저장하기
soup = BeautifulSoup(resp.text)

news_box = soup.find('ul', class_='list_news')
news_list = soup.find_all('li', class_='bx')
print(len(news_list))

'''
[css]
class : '.'
id : '#'
'''
sample = soup.select('.bx')
print(len(sample))
# 태그까지 명시
sample2 = soup.select('li.bx')
print(len(sample2))

sample3 = soup.select('#sp_nws1') # 모든 태그
print(len(sample3))
# 태그까지 명시
sample4 = soup.select('li#sp_nws1') # li 태그
print(len(sample4))

sample5 = soup.select('.news_area a') # news_area 안에 있는 모든 a 태그
print(len(sample5))

sample6 = soup.select('.news_area > a') # news_area 바로 밑에 있는 a 태그 하나만
print(len(sample6))

news_list = soup.select('ul.list_news > li.bx')
print(len(news_list))


result_list = []
# 4. (1~3)을 3페이지까지 반복시키기
for i in range(1, 4):
    params['start'] = i*10 + 1
    resp = requests.get(url, params=params)
    soup = BeautifulSoup(resp.text)

    news_list = soup.select('ul.list_news > li.bx')
    print(len(news_list))


    for news in news_list:
        img_tag = news.select_one('dsc_thumb > img.thumb')
        img = None
        if img_tag:
            img = img_tag.get('src')

        news_dict = {
            'url' : news.select_one('a.news_tit').get('href'),
            'title' : news.select_one('a.news_title').text,
            'desc' : news.select_one('.dsc_txt_wrap').text,
            'thumbnail' : news.select_one('dsc_thumb > img.thumb').get('src')
        }
        result_list.append(news.dict)

    print(len(result_list))
    print(result_list)


# 5. 저장된 결과를 반복하면서 상세페이지의 html가져오기
for item in result_list:
    resp = requests.get(item['url'])
    item['contents'] = resp.text

print(len(result_list))
print(result_list)


