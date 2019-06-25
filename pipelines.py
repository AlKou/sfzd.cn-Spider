# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests

class ChineseChrPipeline(object):
    def process_item(self, item, spider):
        for k, v in item['jpgUrl'].items():
            
            # Download jpg files to destination folder
            data = requests.get(k)
            with open('/Users/Al_gou/Desktop/Scraped/Pics/{}_{}.jpg'.\
                      format(k[7:].replace('/', '-'), v), 'wb') as f:
                f.write(data.content)
            
            # Write scraped urls to destination file
            with open('/Users/Al_gou/Desktop/Scraped/urls.csv', 'a') as f:
                f.write(k + '\t' + v + '\n')
        # Add parsed character to a destination file    
        with open('/Users/Al_gou/Desktop/Scraped/parsed.txt', 'a') as f:
            f.write(item['chr_parsed'])
        
        # Store character with no results to a destination file
        with open('/Users/Al_gou/Desktop/Scraped/nodata.txt', 'a') as f:
            f.write(item['chr_nodata'])
