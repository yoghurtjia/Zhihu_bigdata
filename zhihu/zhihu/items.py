# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ZhihuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()  #用户的个人主页
    name = Field()  #用户的名字
    aggree_count = Field()  #用户获得的赞同数
    thanks_count = Field()   #用户获得的感谢数
    most_good_topic = Field() #从用户的擅长话题中选取一个最擅长的

