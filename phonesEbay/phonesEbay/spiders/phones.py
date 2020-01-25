# -*- coding: utf-8 -*-
import scrapy
import time

from selenium import webdriver

from  phonesEbay.items import PhonesebayItem


class phonesEbay(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['ebay.com']
    start_urls = ['https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094?_sacat=9355']

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    linksToArticles = []

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='../../geckodriver/geckodriver', timeout=10)
        self.driver.get('https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094?_sacat=9355')

  
    def parse(self, response):
        try:
            self.driver.get(response.url)
            next = self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div/div/div/ul/div/div/li[4]/div/div/button')
            next.click()
            time.sleep(2)

            brand = self.driver.find_elements_by_xpath('/html/body/div[11]/div[2]/div/form/div[1]/div[2]/div[1]/div/fieldset/div/div/label/span[1]')
            for b in brand:
                item = PhonesebayItem()
                item['name'] = b.text
                print(item['name'])
                yield item

        except Exception as e:
            print(e)

        # self.driver.quit()
        





        

        








