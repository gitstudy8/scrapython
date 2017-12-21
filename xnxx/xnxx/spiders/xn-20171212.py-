# -*- coding: utf-8 -*-
import scrapy
from xnxx.items import XnxxItem
import re
import json
import requests
from bs4 import BeautifulSoup  #导入库


class XnSpider(scrapy.Spider):
    name = 'xn'
    allowed_domains = ['www.xnxx.com']
    start_urls = ['http://www.xnxx.com/best/2017-11/']

    def parse(self, response):
        videos = response.css('.thumb-block')
        for video in videos:
            item = XnxxItem()
            title = video.css('.thumb-under a::text').extract_first()
            duration = video.css('.thumb-under .duration::text').re_first('\((.*)\)')
            frequency = video.css('.thumb-under .metadata::text').re_first('(.*)hits').strip()
            video_url = video.css('.thumb-under a::attr(href)').extract_first()
            img_src = video.css('.thumb-inside img::attr(data-src)').extract_first()
            videoid = video.css('.thumb-inside img::attr(data-videoid)').extract_first()

            item['title'] = title
            item['duration'] = duration
            item['frequency'] = frequency
            item['video_url'] = video_url
            item['img_src'] = img_src
            item['videoid'] = videoid
            yield item


        next_all = response.css('.pagination .no-page::attr(href)').extract()
        if len(next_all) == 2:
            url = response.urljoin(next_all[1])
        else:
            url = response.urljoin(next_all[3])
        print('--url=' + url)
        print('---next_all'+str(len(next_all)))

        # url = 'http://www.xnxx.com/best/2017-11/1'
        yield scrapy.Request(url=url, callback=self.parse)
         # 回调自己，翻页
    # def parse2(self, response):
    #     a=response.xpath('//*[@id="video-player-bg"]/script[5]/text()').re_first('setVideoUrlHigh\((.*)\)')
    #     print(a)
    #     return a


