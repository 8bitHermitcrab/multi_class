import requests
from bs4 import BeautifulSoup
import csv

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}


def create_soup(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


# [헤드라인 뉴스]
# 1. 뉴스
# (링크 : https)
# 2. 뉴스
# (링크 : https)
# 3. 뉴스
# (링크 : https)

def scrape_headline_news():
    print('[헤드라인 뉴스]')
    # url = 'https://news.naver.com'
    url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'
    soup = create_soup(url)
    # news_list = soup.find('ul', attrs={'class':'hdline_article_list'}).find_all('li', limit=3)
    # news_list = soup.find('ul', attrs={'class':'cluster_text_headline nclicks(cls_sci.clsart)'})
    news_list = soup.find('div', 'list_body')

    for a in news_list.find_all('a'):
        print(a.get_text())
    return None

'''
    for index, news in enumerate(news_list):
        # title = news.div.a.get_text()
        title = news.find('a').get_text().strip()
        link = url + news.find('a')['href']
        print('{}. {}'.format(index+1, title))
        print('  (링크 : {})'.format(link))
    print('---')
'''

def scrape_tech_NYnews():
    url = 'https://www.nytimes.com/section/technology'
    soup = create_soup(url)
    news_list = soup.find('div')
    for a in news_list.find_all('h2'):
        print(a.get_text())
    return None


if __name__ == "__main__":
    # scrape_headline_news()
    scrape_tech_NYnews()