# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class YjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    name=scrapy.Field()
    id=scrapy.Field()
    video_url = scrapy.Field()
    img = scrapy.Field()
    length = scrapy.Field()
    frequency = scrapy.Field()
    rating = scrapy.Field()

    hd = scrapy.Field()
    Crawling_time1 = scrapy.Field()
    Crawling_date = scrapy.Field()
    Upload_time1 = scrapy.Field()
    Upload_date = scrapy.Field()

