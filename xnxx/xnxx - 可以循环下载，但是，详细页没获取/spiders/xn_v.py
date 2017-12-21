# -*- coding: utf-8 -*-
import scrapy
import re
import json

class XnVSpider(scrapy.Spider):
    name = 'xn_v'
    allowed_domains = ['www.xnxx.com']
    start_urls = ['http://http://www.xnxx.com/video-j0mu338/chinese_/']

    def parse(self, response):
        response.xpath('//*[@id="video-player-bg"]/script[5]/text()').re_first('setVideoUrlHigh\((.*)\)')

