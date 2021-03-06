import csv
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
filename = '시총top200.csv'

# encording을 안 넣으면 윈도우OS의 경우 한글이 깨질 수 있음
# newline='' : 한칸씩 띄우는 걸 없애준다
with open('220208/output/'+filename, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)

    #title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split('t')
    title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split('\t')
    writer.writerow(title)

    for page in range(1, 5):
        res = requests.get(url + str(page))
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')

        # table 밑에 tbody, tbody 밑에 tr을 모두 찾는다.
        data_rows = soup.find('table', attrs={'class' : 'type_2' }).find('tbody').find_all('tr')

        for row in data_rows:
            # td값을 하나씩 가져온다
            columns = row.find_all('td')
            if len(columns) <= 1:
                # print('의미없는 데이터')
                continue

            # column의 공백 제거 텍스트를 가져온다
            data = [column.get_text().strip() for column in columns]

            writer.writerow(data)