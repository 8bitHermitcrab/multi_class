import scrapy
from youth.youth.items import YouthItem
 
 
class YouthSpider(scrapy.Spider):
    name = 'YouthCralwer'
 
    def start_requests(self):
        url = 'https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifDtl.do'
        scrapy.Request(url=url)

 
    def parse(self, response, **kwargs):
        items = YouthItem()
        need_path = {
            'category': 'div[1]/div[2]/p[1]/a/text()',
            'title': 'div[1]/div[2]/h1/text()',
            'date': 'div[1]/div[2]/div/p[@class="date"]/text()',
            'tags': 'div[3]/div/a/text()',
            'contents': 'div[2]/div[1]/p/text()',
        }
 
        sel = response.xpath('//*[@id="main"]/div/div[1]/ul/li[2]/div/div')
 
        for col, path in need_path.items():
            crawler_contents = sel.xpath(path).extract()
            items[col] = [contents.strip() for contents in crawler_contents if len(contents.strip()) != 0]
 
        yield items



<!-- <script src="https://2030.go.kr/static/yth/js/iframe_comm.js"></script> -->
<script src="/js/youthcenter.snsLogin.js"></script>

/js/youthcenter.snsLogin.js


<a href="#" id="dtlLink_R2022031900083" onclick="f_Detail('R2022031900083');">							
						<strong>청년 취창업 아카데미</strong>
					</a>