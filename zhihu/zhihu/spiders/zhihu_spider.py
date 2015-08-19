#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
一个简单的Python爬虫, 用于抓取coursera网站的下载链接和pdf

Anthor: Andrew Liu
Version: 0.0.2
Date: 2014-12-15
Language: Python2.7.8
Editor: Sublime Text2
Operate: 具体操作请看README.md介绍
"""
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request, FormRequest
from zhihu.items import ZhihuItem
from scrapy.linkextractors import LinkExtractor


class ZhihuSipder(CrawlSpider) :
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
        "http://www.zhihu.com"
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow = (r'/question/\d+', )),  follow = True),
        Rule(SgmlLinkExtractor(allow = (r'/people/(\w+-?)+$', )), callback = 'parse_page'),
    )
    num_users = 0
    headers = {
    #"Accept": "*/*",
    #"Accept-Encoding": "gzip,deflate",
    #"Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
    #"Connection": "keep-alive",
    #"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
    #"Referer": "http://www.zhihu.com/"
    }
    #output = open('debug.txt','w+')
    #重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        return [Request("http://www.zhihu.com/#signin", meta = {'cookiejar' : 1}, callback = self.post_login)]

    #FormRequeset出问题了
    def post_login(self, response):
        print 'Preparing login'
        #下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        print xsrf
        #FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        #登陆成功后, 会调用after_login回调函数
        return [FormRequest.from_response(response,   #"http://www.zhihu.com/login",
                            meta = {'cookiejar' : response.meta['cookiejar']},
                            headers = self.headers,
                            formdata = {
                            '_xsrf': xsrf,
                            'email': '1527927373@qq.com',
                            'password': '321324jia'
                            },
                            callback = self.after_login,
                            dont_filter = True
                            )]

    def after_login(self, response) :
        for url in self.start_urls :
            yield self.make_requests_from_url(url)

    def parse_page(self, response):
        self.num_users = self.num_users + 1
        problem = Selector(response)
        item = ZhihuItem()
        item['url'] = response.url    #用户主页
        item['name'] = problem.xpath('//div[@class="title-section ellipsis"]/span[@class="name"]/text()').extract() #用户的名字
        item['aggree_count'] = problem.xpath('//span[@class="zm-profile-header-user-agree"]/strong/text()').extract()#用户得到的同意数目
        item['thanks_count'] = problem.xpath('//span[@class="zm-profile-header-user-thanks"]/strong/text()').extract()#得到的感谢数目
        item['most_good_topic'] = problem.xpath('//div[@class="zm-profile-section-list zg-clear"]/div[1]/div/div/h3/a/text()').extract() #这个用户最擅长的话题 #这个选项可能有些用户是没有的,是空值
        return item
        #print response.url
        #print self.num_users
        #self.output.write(response.url)
        #self.output.write(self.num_users)
        '''url = Field()  #用户的个人主页
        name = Field()  #用户的名字
        
        aggree_count = Field()  #用户获得的赞同数
        thanks_count = Field()   #用户获得的感谢数
        most_good_topic = Field() #从用户的擅长话题中选取一个最擅长的
        '''
        '''item['name'] = problem.xpath('//span[@class="name"]/text()').extract()
        print item['name']
        item['title'] = problem.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        item['description'] = problem.xpath('//div[@class="zm-editable-content"]/text()').extract()
        item['answer']= problem.xpath('//div[@class=" zm-editable-content clearfix"]/text()').extract()
        '''
