# -*- coding: utf-8 -*-
#########################################
# 已实现翻页，详细页面爬去，视频url抓取
# scrapy crawl xn -o xn.csv
'''
Scrapy设置之提前终止爬虫
http://blog.csdn.net/Q_AN1314/article/details/51104701

$ scrapy crawl fast -s CLOSESPIDER_TIMEOUT=10
# CLOSESPIDER_TIMEOUT（秒）在指定时间过后终止爬虫程序
$ scrapy crawl fast -s CLOSESPIDER_ITEMCOUNT=10
# 在抓取了指定数目的Item之后
$ scrapy crawl fast -s CLOSESPIDER_PAGECOUNT=10
# 在收到了指定数目的响应之后
'''
# Scrapy输出CSV指定列顺序 http://www.jianshu.com/p/fd6f7eba6abe
#########################################

import scrapy
from xnxx.items import XnxxItem
import re
import json
import requests
from bs4 import BeautifulSoup  #导入库
from urllib.parse import urljoin
import time
import re
add = 0
class XnSpider(scrapy.Spider):
    name = 'xn'
    allowed_domains = ['www.xnxx.com']
    start_urls = ['http://www.xnxx.com/best/2017-09/']
    # date_best = '2017-11'

    def parse(self, response):
        global add
        videos = response.css('.thumb-block')
        for video in videos:
            # item = XnxxItem()
            # title = video.css('.thumb-under a::text').extract_first()
            duration = video.css('.thumb-under .duration::text').re_first('\((.*)\)')
            # frequency = video.css('.thumb-under .metadata::text').re_first('(.*)hits').strip()
            video_url = urljoin('http://www.xnxx.com', video.css('.thumb-under a::attr(href)').extract_first())
            img_src = video.css('.thumb-inside img::attr(data-src)').extract_first()
            videoid = video.css('.thumb-inside img::attr(data-videoid)').extract_first()

            # item['title'] = title
            # item['duration'] = duration
            # item['frequency'] = frequency
            # item['video_url'] = video_url
            # item['img_src'] = img_src
            # item['videoid'] = videoid
            ## 将得到的页面地址传送给单个页面处理函数进行处理 -> parse_content()
            # print('------11111-----------------')
            # print(video_url)

            # print('------2222-----------------')
            # yield item
            add += 1
            # print('------3333add-----------------'+str(add))
            yield scrapy.Request(video_url, callback=self.parse_content, meta={'img_src': img_src,'videoid': videoid,'id':add,'duration':duration})
            ### 传参成功
            ### 参考：http://www.jianshu.com/p/de61ed0f961d
            # yield scrapy.Request(video_url, callback=self.parse_content)
            # print('------4444-----------------')

        next_all = response.css('.pagination .no-page::attr(href)').extract()
        if len(next_all) == 2:
            url = response.urljoin(next_all[1])
        else:
            url = response.urljoin(next_all[3])
        # print('--url=' + url)
        # print('---next_all'+str(len(next_all)))
        # print('------5555----------------')
        # url = 'http://www.xnxx.com/best/2017-11/1'
        yield scrapy.Request(url=url, callback=self.parse)
         # 回调自己，翻页
    def parse_content(self,response):
        # print('----66666---')
        item = XnxxItem()
        like = response.css('#video-votes .vote-action-good .value::text').extract_first()
        notlike = response.css('#video-votes .vote-action-bad .value::text').extract_first()
        video_download = response.xpath('//*[@id="video-player-bg"]/script[5]/text()').re_first('setVideoUrlHigh\(\'(.*)\'\)')
        Introduction1 = response.css('#video-content-metadata div p::text').extract_first()
        if Introduction1 is not None:
            # Introduction=Introduction1.strip('\"\,\t\n\r')
            # Introduction=eval(Introduction1)
            Introduction=re.sub(r'^"|"$', '', Introduction1)
            #去掉双引号eval
        else:
            Introduction=''
        star  = response.css('#video-votes .metadata-btn .rating-box.value::text').extract_first()
        tags1  = response.css('#video-content-metadata .metadata-row.video-tags a::text').extract()
        tags = ';'.join(tags1)
        img_src = response.meta['img_src']
        videoid = response.meta['videoid']
        id = response.meta['id']
        # print('========='+str(like))
        title1= response.css('#video-content-metadata .infobar strong::text').extract_first()
        title = re.sub(r'^"|"$', '', title1)
        # item['duration'] = response.css('#video-content-metadata .metadata-btn .value::text').extract_first()
        item['duration'] = response.meta['duration']
        item['frequency'] = response.css('#nb-views-number::text').extract_first()
        item['video_url'] = response.url
        item['img_src'] = img_src
        item['videoid'] = videoid
        item['title'] = title
        # item['Introduction'] = Introduction
        item['video_download'] = video_download
        item['notlike'] = notlike
        item['like'] = like
        item['star'] = star
        item['tags'] = tags
        item['id'] = id
        item['date_best'] = '201709'
        item['Crawling_date'] = time.strftime('%Y%m%d')
        yield item
