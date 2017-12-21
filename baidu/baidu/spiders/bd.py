# -*- coding: utf-8 -*-
import scrapy


class BdSpider(scrapy.Spider):
    name = 'bd'
    allowed_domains = ['http://baidu.com']
    start_urls = ['http://http://baidu.com/']

    def parse(self, response):
        pass
