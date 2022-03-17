import requests
from bs4 import BeautifulSoup
import re

##
for i in range(0, 6, 1):

    # url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor='
    url = f'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=1=6&backgroundColor='
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    # print(len(soup.text))

    # search-product 값으로 시작하는 li 태그, 클래스 전부 찾기
    items = soup.find_all('li', attrs={'class' : re.compile('^search-product')})

    # print(items)

    # print(items[0].find('div', attrs={'class' : 'name'}).get_text())

    ##
    print('페이지 : ', i)

    for item in items:
        # 제품명
        name = item.find('div', attrs={'class' : 'name'}).get_text()
        #
        name = name.split(', ')[0]
        # 가격
        price = item.find('strong', attrs={'class' : 'price-value'}).get_text()
        # 평점
        rate = item.find('em', attrs={'class' : 'rating'})
        if rate : 
            rate = rate.get_text()
        else:
            rate = '평점 없음'
        # 리뷰수
        rate_count = item.find('span', attrs={'class' : 'rating-total-count'})
        if rate_count : 
            rate_count = rate_count.get_text()
            ## rate_count = rate_count.get_text()[1:-1]
        else:
            rate_count = '리뷰수 없음'

        # 쿠팡 추천 제외
        coupang_recommend = item.find('img', attrs={'class' : 'badge-ico badge-coupick'})
        # 광고 제외
        ad = item.find('span', attrs={'class' : 'ad-badge'})
        if ad or coupang_recommend:
            # ad = '광고 o'
            # coupang_recommend = '쿠팡 추천 o'
            continue
        else:
            ad = '광고 x'
            coupang_recommend = '쿠팡 추천 x'
            print('제품명 : ', name)
            print('가격 : ', price)
            print('평점 : ', rate)
            print('리뷰수 : ', rate_count)
            print('='*80)
        #print('광고 : ', ad)
        #print('='*80)
        # print(name, price, rate, rate_count)
        # pages = item.find('div', attrs={'class' : 'search-pagination'})
        # print(pages.text)
        # for page in pages:
        #     # page_num = page.text.strip()
        #     print(pages.text)

        


    # if page in ['이전', '다음']:
    #    continue
    # else:
    #    print(page)