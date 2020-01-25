# -*- coding: utf-8 -*-
import scrapy
from  phones.items import PhonesItem

class Phones(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['mobilni-telefony.heureka.cz']
    start_urls = ['https://mobilni-telefony.heureka.cz/f:2479:101172,101170,16317348/']

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
  
    def parse(self, response):
        try:
            text = response.xpath('(//div[@class="attr-values"])[3]//text()').extract()
            text = list(dict.fromkeys(text))
            for x in text:
                item = PhonesItem()
                if "\n" not in x.lower() and '(' not in x.lower() and 'více' not in x.lower():
                    item['name'] = x
                    yield item
                    
        except Exception as e:
            print(e)

        





        

        








