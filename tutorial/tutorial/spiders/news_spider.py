import scrapy
from scrapy.exporters import JsonLinesItemExporter
from tutorial.items import TutorialItem

# Scrapy Spider
class FinNewsSpider(scrapy.Spider):
    # Initializing log file
    # logfile("news_spider.log", maxBytes=1e6, backupCount=3)
    name = "news_spider"
    allowed_domains = ['benzinga.com/']
    start_urls = [
        'https://www.benzinga.com/top-stories/20/09/17554548/stock-wars-ford-vs-general-motors-vs-tesla'
    ]

# MY SCRAPY STUFF
# response.xpath('//div[@class="article-content-body-only"]/p/text()').extract()
    def parse(self, response):
        paragraphs = response.xpath('//div[@class="article-content-body-only"]/p/text()').extract()
        print(paragraphs)
        yield TutorialItem(content=paragraphs)
        ##### If I want to break up each p in a dict
        # for p in paragraphs:
        #     yield TutorialItem(content=p)
