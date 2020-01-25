# -*- coding: utf-8 -*-
import scrapy
from  phonesPhonesData.items import PhonesphonesdataItem

class PhonesPhonesData(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['phonesdata.com']
    start_urls = ['http://phonesdata.com/en/smartphones/']

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
  
    def parse(self, response):
        stop = ['\n', '[', ']', '(', ')', 'více', 'devices', ' ']
        try:
            text = response.xpath('//div[@class="col-md-1 col-sm-1 col-xs-1"]//p//text()').extract()  
            text = list(dict.fromkeys(text))
            for word in text:
                item = PhonesphonesdataItem()
                if not any([x in word for x in stop]):
                    item['name'] = word
                    yield item
                    
        except Exception as e:
            print(e)

        





        

        








