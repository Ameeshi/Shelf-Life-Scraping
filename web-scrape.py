from scrapy import Request
from scrapy.spiders import Spider

class MySpider(Spider):
    name = 'a2'
    start_urls = ['https://food.unl.edu/food-storage-chart-cupboardpantry-refrigerator-and-freezer/']

    def parse(self, response):
        rows = response.xpath('//div[@class="journal-content-article"]/table/tbody/tr')
        items=[]
        for row in rows:
            item = {}
            item['food'] = row.xpath('./td[1]/text()').extract()
            item['pantry'] = row.xpath('./td[2]/text()').extract()
            item['refrigerator'] = row.xpath('./td[3]/text()').extract()
            item['freezer'] = row.xpath('./td[4]/text()').extract()
            items.append(item)      
        return items 