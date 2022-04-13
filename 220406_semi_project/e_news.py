import requests
from bs4 import BeautifulSoup
import csv, xls
import pandas as pd

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}


def create_soup(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def scrape_tech_NYnews():
    url = 'https://www.nytimes.com/section/technology'
    soup = create_soup(url)
    news_list = soup.find('div')
    for a in news_list.find_all('h2'):
        # print(a.get_text())
        title = a.get_text()
        # for index, news in enumerate(news_list):
        #     title = news.find('a').get_text().strip()
        #     print('{}. {}'.format(index+1, title))
        filename = 'e_news.xls'
        with open('/Users/kij/workspace/220406_semi_project/'+filename, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            # writer = xls.writer(f)
            # title = 'title topic_idx'.split()
            writer.writerow(title)

            # writer = pd.ExcelWriter(f)
            # writer.writerow(title)
    return None


if __name__ == "__main__":
    scrape_tech_NYnews()