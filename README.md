>项目介绍

> 自己封装的简单的爬虫框架，使用方式和scrapy框架的使用方式大致相同

>技术栈

1. httpx:一个支持异步和HTTP1.0和HTTP2.0的异步请求库，主要用来发送网络请求
2. lxml:解析xml和html文本的第三方库
3. asyncio: python内置库，使用async/await语法实现协程

> 运行项目

> python crawl --crawl main

这条命令会在项目根目录下寻找main.py文件，并且在其中搜索Spider的类的子类，利用Spider类start_request方法
发起异步请求，并且调用指定的callback回调函数(默认是parse方法)实现内容的解析，如果需要指定自己的回调函数，需要
手动构造Request对象并且指定callback参数