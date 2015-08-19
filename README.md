# overview
使用scrapy和pandas完成对知乎300w用户的数据分析。首先使用scrapy爬取知乎网的300w，用户资料，   
最后使用pandas对数据进行过滤，找出想要的知乎大牛，并用图表的形式可视化。  
#requirments:
os:win7 64bit  
scrapy:1.0  
python：2.7.10  
anaconda:安装这个，可以使用里面的ipython notebook
#use
1.由于知乎网需要登录，所以如果想要使用这个爬虫，需要有一点scrapy基础。scrapy登陆的时候需要自己的知乎账号和密码，请修改  
zhihu\zhihu\spiders\zhihu_spider.py，里面的 ： 
                           formdata =   
                            {
                            '_xsrf': xsrf,#不需要修改    
                            'email': 'abc@qq.com', #改成自己知乎登陆账号   
                            'password': 'abc'#改成自己的密码   
                            },    
2.下载文件夹到自己的电脑上，打开windows,cmd，cd zhihu:  
scrapy crawl zhihu -o user.json（生成一个user.json文件，里面包含我们需要的用户信息：
json有将近300w条用户信息。每一条的组成结构如下所示：  
url  #用户主页地址  
aggree_count #用户获得的赞同数（越多越牛）
thanks_count #用户得到的感谢数（越多越牛）  
name         #用户名字   
most_good_topic #最感兴趣的话题      
##关于爬虫方面的疑问，请参考这个链接：  
[使用scrapy模拟登陆知乎](http://www.jianshu.com/p/b7f41df6202d)   
##使用pandas对user.json进行数据分析，以及可视化。
关于这部分的代码，我全部放在data_analysis.ipynb，只要计算机上安装了ipython notebook，就可以打开，重现计算结果
                            

