from bs4 import BeautifulSoup
import requests
import json

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
    'Pragma': 'no-cache',
    'X-Content-Type-Options': 'nosniff',
    'X-XSS-Protection': '1; mode=block',
    'Content-Type': 'text/html;charset=utf-8',
    'Date': 'Tue, 03 May 2022 15:21:20 GMT',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }

# sess = requests.session()
detail_p = requests.get(detail_url, headers=headers)
soup = BeautifulSoup(detail_p.text)
print(detail_p.text)