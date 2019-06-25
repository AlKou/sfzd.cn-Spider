# -*- coding: utf-8 -*-
import scrapy
from ChineseChr.items import ChineseChrItem
from scrapy.http import FormRequest
import re
import time

class ChrSpider(scrapy.Spider):
    name = 'chr'
    allowed_domains = ['shufazidian.com']
    start_urls = ['http://www.shufazidian.com/s.php']
            
    def parse(self, response):
        # First read the to-scrape characters into a variable
        with open('/Users/Al_gou/Desktop/Scraped/ChineseChar 3.5K.txt', 'r') as f:
            charSet = f.read()
        
        # Final all needed urls from response, and current character as well.
        urls = re.findall('(http://www.sfzd.cn/zb/jpg/.*?.jpg)',response.text)
        urls = list(set(urls))
        chr = response.xpath('//*[@id="kw"]/@value').extract()[0]
        
        # Initialize the item object to yield
        item = ChineseChrItem()
        item['jpgUrl'] = {}
        item['chr_parsed'] = ''
        item['chr_nodata'] = ''
        
        # Update item values by judging if any result is found.
        if urls:
            for url in urls:
                item['jpgUrl'][url] = chr
            print('@{} >>>>>> {} completed.'.format(time.ctime(), chr))
            item['chr_parsed'] = chr
        else: 
            print('@{} >>>>>> {} no data!'.format(time.ctime(), chr))   
            item['chr_nodata'] = chr
        
        # After processing a character, remove it from the source file.
        with open('/Users/Al_gou/Desktop/Scraped/ChineseChar 3.5K.txt', 'w') as f:
            f.write(charSet.replace(chr, ''))
            
        yield item
        
        # Yield next request with form submition.
        for char in charSet:
            formdata = {'wd': char, 'ziti': 'k', 'leibie': 'mb'}
            time.sleep(0.1)
            yield FormRequest.from_response(response, 
                                            formdata=formdata, 
                                            callback=self.parse)
   