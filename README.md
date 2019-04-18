### 爬虫（高级）
##### 1、任务一：构建请求
对页面进行分析后股票信息为动态加载，分析其原始地址可得到参数为page = x，在发起请求后发现页面拒绝访问，为请求头中添加user-agent，可正常访问。
##### 2、任务二：分析json
要求为爬取涨幅前100的股票信息，其中每页的股票信息为30条，当page=4时，只将前10条数据记入item中。分析json获得股票信息
##### 3、任务三：格式化输出
添加excel数据输出格式
```
scrapy crawl stock -t excel -o stock.xls
scrapy crawl stock -o stock.csv
```
