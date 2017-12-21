# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XnxxItem(scrapy.Item):
    title = scrapy.Field()
    id = scrapy.Field()
    duration = scrapy.Field()
    frequency = scrapy.Field()
    video_url = scrapy.Field()
    img_src = scrapy.Field()
    videoid = scrapy.Field()
    like = scrapy.Field()
    notlike = scrapy.Field()
    video_download = scrapy.Field()
    # hd = scrapy.Field()
    Introduction = scrapy.Field()
    star = scrapy.Field()
    tags = scrapy.Field()
    date_best = scrapy.Field()
    Crawling_date = scrapy.Field()
