import scrapy
from scrapy import Request
from AmericaStock.items import AmericastockItem
import json
class stock_spider(scrapy.Spider):
    name = 'stock'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    start_urls = ['https://xueqiu.com/service/v5/stock/screener/quote/list?page={}&size=30&order=desc&orderby=chg&order_by=chg&market=US&type=us&_=1555060351777'.format(str(i)) for i in range(1, 5)]
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url,headers=self.header)
    def parse(self, response):

        js = json.loads(response.body.decode('utf-8'))
        if 'page=4' in response.url:
            i = 0
            for each_js in js['data']['list']:
                i +=1
                if i>= 11:
                    break
                item = AmericastockItem()
                item['symbol'] = each_js['symbol']
                item['name'] = each_js['name']
                item['current'] = each_js['current']
                item['chg'] = each_js['chg']
                item['market_capital'] = each_js['market_capital']
                item['pe_ttm'] = each_js['pe_ttm']
                yield item
        else:
            for each_js in js['data']['list']:
                item = AmericastockItem()
                item['symbol']  =  each_js['symbol']
                item['name'] =  each_js['name']
                item['current'] = each_js['current']
                item['chg'] = each_js['chg']
                item['market_capital'] = each_js['market_capital']
                item['pe_ttm'] = each_js['pe_ttm']
                yield item



