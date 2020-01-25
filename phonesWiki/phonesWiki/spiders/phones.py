# -*- coding: utf-8 -*-
import scrapy
from  phonesWiki.items import PhoneswikiItem

class PhonesWiki(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_mobile_phone_brands_by_country']

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
  
    def parse(self, response):
        stop = ['\n', '[', ']', '(', ')', 'více']
        try:
            text = response.xpath('/html/body/div[3]/div[3]/div[4]/div/table[1]//tr//td[2]//text()').extract()
            text = list(dict.fromkeys(text))
            for word in text:
                item = PhoneswikiItem()
                if not any([x in word for x in stop]):
                    item['name'] = word
                    yield item
                    
        except Exception as e:
            print(e)

        





        

        








