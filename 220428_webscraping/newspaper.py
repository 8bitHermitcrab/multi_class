# newspaper3k

import requests
from bs4 import BeautifulSoup

# !pip install newspaper3k

url = 'https://search.naver.com/search.naver'
params = {
    'where': 'news',
    'query': '무역전쟁'
}

result_list = []
# (1~3)을 3페이지까지 반복시키기
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


# 저장된 결과를 반복하면서 상세페이지의 html가져오기
for item in result_list:
    resp = requests.get(item['url'])
    item['contents'] = resp.text

print(len(result_list))
print(result_list)


news_result_list = result_list.copy()
news = news_result_list[0]
print(news)

from newspaper import Article

article = Article(news['url'])
print(article.download())
print(article.parse())
print(article.title)
print(article.text)
# dir(article) # 함수 확인
print(article.images)
print(article.publish_date)