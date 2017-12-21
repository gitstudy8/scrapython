# -*- coding: utf-8 -*-
#########################################
# scrapy crawl yj_scrapy -o yj.csv
#########################################
import scrapy
from yj.items import YjItem
import time
import datetime
Crawling_time1=time.strftime('%Y%m%d %H:%M:%S')
# Crawling_time1=datetime.datetime.now()
# Crawling_time1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# Crawling_time2=time.strftime("%Y-%m-%d", time.localtime())
Crawling_date=time.strftime('%Y%m%d')
# Crawling_date=datetime.date.today()
# print(Crawling_date)
class YjScrapySpider(scrapy.Spider):
    name = 'yj_scrapy'
    allowed_domains = ['www.yjizz.tv']
    start_urls = ['http://www.yjizz.tv/recent/']
    # page_num = 1

    def parse(self, response):
        # pass
        # pass 默认回调方法
        # print("response.text")
        # videos = response.css('li[id*=video]')
        videos = response.css('.video')
        num=0
        for video in videos:
            item=YjItem()
            #在items.py中定义的
            name = video.css('.video-title a::text').extract_first()
            #进一步筛选quote
            #::是特有的语法结构，是输出text中文本
            #extract_first找第一个结果
            img = video.css('.video-thumb img[src*=jpg]::attr(src)').extract_first()
            video_url = video.css('.video-title a::attr(href)').extract_first()
            id = video.css('.video-title a::attr(href)').re_first('[0-9]+')
            hd = video.css('.video-overlay span::text').extract_first()
            if hd=='HD':
                length = video.css('.video-overlay::text').extract()[1].strip()
            else:
                hd = 'No-HD'
                length = video.css('.video-overlay::text').extract_first().strip()
            # length = video.css('.video-overlay::text').re_first('.*\"(.*)\"')
            rating = video.css('.rating::text').re_first('(.*)%').strip()

            # frequency = video.css('.clearfix::text').extract()[3].strip()
            frequency = video.css('.clearfix::text').re_first('(.*)次播放').strip()
            Upload_time1 = video.css('.time::text').extract_first()
            if Upload_time1=='today':
                Days=0
            else:
                # Days=video.css('.time::text').re_first('(.*)天').strip()
                Days=1

            # print('----today-1--------:' + str(datetime.date.today()-datetime.timedelta(days = int(Days))))
            Upload_date = datetime.date.today()-datetime.timedelta(days = int(Days))
            # Upload_date=datetime.strftime('%Y-%m-%d',Upload_date)
            num = num + 1
            # print('page_num:'+str(page_num)+'--num:'+str(num))
            print('num:'+str(num))
            item['name'] = name
            item['id'] = id
            item['img'] = img
            item['video_url'] = video_url
            item['length'] = length
            item['hd'] = hd
            item['rating'] = rating
            item['frequency'] = frequency
            item['Crawling_date'] = Crawling_date
            item['Crawling_time1'] = Crawling_time1
            item['Upload_time1'] = Upload_time1
            item['Upload_date'] = Upload_date.strftime('%Y%m%d')
            yield item

        #下一页提取
        # next = response.css('.pagination .prevnext::attr(href)').extract_first()
        next_all = response.css('.pagination .prevnext::attr(href)').extract()
        if len(next_all)==1:
            url = response.urljoin(next_all[0])
        else:
            url = response.urljoin(next_all[1])
        print('--url='+url)
        # url = 'http://www.yjizz.tv/recent/2/'
        # page_num=page_num+1
        yield scrapy.Request(url=url, callback=self.parse)
        #回调自己，翻页




