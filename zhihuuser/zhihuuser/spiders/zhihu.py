# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy import Request
# 直接从scrapy引入，后面就不用每次都写scrapy.Request


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']


    def star_requests(self):
        url = 'https://www.zhihu.com/api/v4/members/gua-gua-lai-liao?include=allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'
        yield Request(url, callback=self.parse)

    def parse(self, response):
        print(response.text)
