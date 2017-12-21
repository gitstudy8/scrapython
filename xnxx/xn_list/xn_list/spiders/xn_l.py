# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
from xn_list.items import XnListItem

class XnLSpider(scrapy.Spider):
    name = 'xn_l'
    allowed_domains = ['www.xnxx.com']
    start_urls = ['http://www.xnxx.com/video-gc5m996/chinese_pretty_girl_-_javshare99.net/','http://www.xnxx.com/video-gakxtab/hot_girl_korean_chat_sex_new_2017']


    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        for h3 in hxs.css('#video-content-metadata .infobar strong::text').extract_first():
            item = XnListItem()
            item['title'] = h3
            yield item()
            # yield XnListItem(title=h3)

        for url in hxs.select('//a/@href').extract():
            yield Request(url, callback=self.parse)

        for url in self.start_urls:
            title = response.css('#video-content-metadata .infobar strong::text').extract_first()
            # print('------'+str(title))
            item = XnListItem()
            item['title'] = title
            yield item
        yield scrapy.Request(url=url, callback=self.parse)
