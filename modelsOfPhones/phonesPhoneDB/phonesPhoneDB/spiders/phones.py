# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from  phonesPhoneDB.items import PhonesphonedbItem

class PhonesPhoneDB(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['phonedb.net']
    start_urls = ['http://phonedb.net/index.php?m=device&s=list']

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse_mobiles(self, response):
        try:
            devicesOnPage = response.xpath('/html/body/div[5]/div').extract() 

            for device in devicesOnPage:
                if 'smartphone' in device.lower():
                    sel = Selector(text="%s" % (device)) 
                    name = sel.xpath('//div[@class="content_block_title"]//a//text()').extract()
                    item = PhonesphonedbItem()
                    item['name'] = name[0].lower()
                    yield item

        except Exception as e:
            print(e)

    def parse(self, response):
        try:
            basicUrl = 'http://phonedb.net'
            url = response.xpath('/html/body/div[7]/a/@href').extract()
            textsUrl = response.xpath('/html/body/div[7]/a/text()').extract()

            x = 0
            text = textsUrl[x]
            while(text.lower() != 'next'):
                yield scrapy.Request(url=basicUrl + url[x], callback=self.parse_mobiles)
                x = x + 1
                text = textsUrl[x]
                    
        except Exception as e:
            print(e)

        





        

        








