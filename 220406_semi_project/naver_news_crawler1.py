import requests
from bs4 import BeautifulSoup

# url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1='
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

# topic = {'IT과학' : 0, '경제' : 1, '사회' : 2, '생활문화' : 3, '세계' : 4, '스포츠' : 5, '정치' : 6}

# topic, topic_idx
# 'IT과학' : 0 = <a href="https://news.naver.com/main/main.naver?mode=LSD&amp;mid=shm&amp;sid1=105" class="Nitem_link" role="menuitem" aria-selected="false" onclick="nclk(event,'lnb.sci','','');"><span class="Nitem_link_menu">IT/과학</span></a>
# '경제' : 1 = <a href="https://news.naver.com/main/main.naver?mode=LSD&amp;mid=shm&amp;sid1=101" class="Nitem_link" role="menuitem" aria-selected="false" onclick="nclk(event,'lnb.eco','','');"><span class="Nitem_link_menu">경제</span></a>
# '사회' : 2 = <a href="https://news.naver.com/main/main.naver?mode=LSD&amp;mid=shm&amp;sid1=102" class="Nitem_link" role="menuitem" aria-selected="false" onclick="nclk(event,'lnb.soc','','');"><span class="Nitem_link_menu">사회</span></a>
# '생활문화' : 3 = <a href="https://news.naver.com/main/main.naver?mode=LSD&amp;mid=shm&amp;sid1=103" class="Nitem_link" role="menuitem" aria-selected="false" onclick="nclk(event,'lnb.lif','','');"><span class="Nitem_link_menu">생활/문화</span></a>
# '세계' : 4 = <a href="https://news.naver.com/main/main.naver?mode=LSD&amp;mid=shm&amp;sid1=104" class="Nitem_link" role="menuitem" aria-selected="false" onclick="nclk(event,'lnb.wor','','');"><span class="Nitem_link_menu">세계</span></a>
# '스포츠' : 5 = <a href="https://sports.news.naver.com/index" onclick="nclk(event,'gnb.sports','','');">
# '정치' : 6 = <a href="https://news.naver.com/main/main.naver?mode=LSD&amp;mid=shm&amp;sid1=100" class="Nitem_link" role="menuitem" aria-selected="false" onclick="nclk(event,'lnb.pol','','');"><span class="Nitem_link_menu">정치</span></a>

i = f'숫자를 입력하세요(IT과학 : 0, 경제 : 1, 사회 : 2, 생활문화 : 3, 세계 : 4, 스포츠 : 5, 정치 : 6): {int(input())}'

# 'IT과학' : 0 // 105
if i == 0:
    url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'
    # URL과 헤더를 get으로 가져오기
    res = requests.get(url, headers=headers)
    # 오류 확인
    res.raise_for_status()

    # bs4로 페이지 분석
    soup = BeautifulSoup(res.text, 'lxml')

    a_it = soup.find('a', attrs={'class':'cluster_text_headline nclicks(cls_sci.clsart)::before'})
    print(a_it)
    

    
# '경제' : 1 // 101
elif i == 1: 
    # topic_num = '101'
    # url = url + topic_num
    url = 'https://news.naver.com/main/main.naver?mode=LSD&amp;mid=shm&amp;sid1=101'
    
# '사회' : 2 // 102
elif i == 2:
    # topic_num = '102'
    # url = url + topic_num
    url = 'https://news.naver.com/main/main.naver?mode=LSD&amp;mid=shm&amp;sid1=102'
    
# '생활문화' : 3 // 103
elif i == 3:
    # topic_num = '103'
    # url = url + topic_num
    url = 'https://news.naver.com/main/main.naver?mode=LSD&amp;mid=shm&amp;sid1=103'

# '세계' : 4 // 104
elif i == 4:
    # topic_num = '104'
    # url = url + topic_num
    url = 'https://news.naver.com/main/main.naver?mode=LSD&amp;mid=shm&amp;sid1=104'

# '정치' : 6 // 100
elif i == 6:
    # topic_num = '100'
    # url = url + topic_num
    url = 'https://news.naver.com/main/main.naver?mode=LSD&amp;mid=shm&amp;sid1=100'

# '스포츠' : 5
else:
    url = 'https://sports.news.naver.com/index'

# URL과 헤더를 get으로 가져오기
res = requests.get(url, headers=headers)
# 오류 확인
res.raise_for_status()

# bs4로 페이지 분석
soup = BeautifulSoup(res.text, 'lxml')

table = soup.find('a', attrs={'class':'cluster_text_headline nclicks(cls_pol.clsart)'})
print(table)

a_it = soup.find('a', attrs={'class':'cluster_text_headline nclicks(cls_sci.clsart)'})
print(a_it)


# https://domdom.tistory.com/entry/%ED%81%AC%EB%A1%A4%EB%A7%81-BeautifulSoup-%EC%9C%BC%EB%A1%9C-%EA%B0%80%EC%A0%B8%EC%98%A8-%EB%8D%B0%EC%9D%B4%ED%84%B0-CSV%EC%97%91%EC%85%80%ED%8C%8C%EC%9D%BC%EB%A1%9C-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0