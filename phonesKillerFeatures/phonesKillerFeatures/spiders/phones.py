# -*- coding: utf-8 -*-
import scrapy
from  phonesKillerFeatures.items import PhoneskillerfeaturesItem

class Phoneskillerfeatures(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['killerfeatures.com']
    start_urls = ['https://www.killerfeatures.com/list-of/mobile/latest-new-mobiles-price-list']

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
  
    def parse(self, response):
        stop = ['\n', '[', ']', '(', ')', 'více', 'devices', ' ']
        try:
            text = response.xpath('//*[@id="brandMainDiv"]//li//text()').extract()   
            text = list(dict.fromkeys(text))
            for word in text:
                item = PhoneskillerfeaturesItem()
                if not any([x in word for x in stop]):
                    item['name'] = word
                    yield item
                    
        except Exception as e:
            print(e)

        





        

        








