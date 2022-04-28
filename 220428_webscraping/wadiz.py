# 와디즈 데이터 수집

import requests
from bs4 import BeautifulSoup
import json

# headers = {
#     'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
#     'cookie' : '',
#     '' : '',
#     '' : ''
# }

url = 'https://www.wadiz.kr/web/wreward/ajaxGetCardList'
params = {
    'keword' : '',
    'endYn' : 'ALL',
    'order' : 'recommend',
    'startNum' : '720',
    'limit' : '48'
}
resp = BeautifulSoup(url, params
    # headers=headers
)
print(resp.text)

data2 = json.loads() # JSON(string) -> python object
print(data2)