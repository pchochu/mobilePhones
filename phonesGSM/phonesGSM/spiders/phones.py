# -*- coding: utf-8 -*-
import scrapy
from  phonesGSM.items import PhonesgsmItem

class PhonesWiki(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['gsmarena.com']
    start_urls = ['https://www.gsmarena.com/makers.php3']

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
  
    def parse(self, response):
        stop = ['\n', '[', ']', '(', ')', 'více', 'devices']
        try:
            text = response.xpath('//div[@class="st-text"]//table//tr//td//a//text()').extract() 
            text = list(dict.fromkeys(text))
            for word in text:
                item = PhonesgsmItem()
                if not any([x in word for x in stop]):
                    item['name'] = word
                    yield item
                    
        except Exception as e:
            print(e)

        





        

        








