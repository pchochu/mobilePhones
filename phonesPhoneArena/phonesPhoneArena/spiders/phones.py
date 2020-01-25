# -*- coding: utf-8 -*-
import scrapy
from  phonesPhoneArena.items import PhonesphonearenaItem

class PhonesPhonesData(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['phonearena.com']
    start_urls = ['https://www.phonearena.com/phones/manufacturers']

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
  
    def parse(self, response):
        stop = ['\n', '[', ']', '(', ')', 'více', 'devices', ' ']
        try:
            text = response.xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div/div/div/a[1]/span//text()').extract()  
            text = list(dict.fromkeys(text))
            for word in text:
                item = PhonesphonearenaItem()
                if not any([x in word for x in stop]):
                    item['name'] = word
                    yield item
                    
        except Exception as e:
            print(e)

        





        

        








