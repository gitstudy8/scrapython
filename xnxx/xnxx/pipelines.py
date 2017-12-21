# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



# from bs4 import BeautifulSoup
# html='http://http://www.xnxx.com/video-j0mu338/chinese_/'
# soup = BeautifulSoup(html, 'lxml')
# print('-------------')
# print(soup.select('.panel .panel-heading'))

class XnxxPipeline(object):
    def process_item(self, item, spider):
        return item


# class vPipeline(object):
#     def process_item(self, item, spider):
#         html=item['video_url']
#         soup = BeautifulSoup(html, 'lxml')
#         print(soup.select('title'))
#         return item