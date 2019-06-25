# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChineseChrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jpgUrl = scrapy.Field()        # To store the urls scraped
    chr_parsed = scrapy.Field()    # To store parsed characters with results
    chr_nodata = scrapy.Field()    # To store parsed characters with no results
