import scrapy
from scrapy.exporters import JsonLinesItemExporter

# Scrapy Spider
class FinNewsSpider(scrapy.Spider):
    # Initializing log file
    # logfile("news_spider.log", maxBytes=1e6, backupCount=3)
    name = "news_spider"
    allowed_domains = ['benzinga.com/']
    start_urls = [
        'https://www.benzinga.com/top-stories/20/09/17554548/stock-wars-ford-vs-general-motors-vs-tesla'
    ]

#### Actually don't have to use the start_requests function since it's built in. Can just use start_urls
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/'
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    # start_urls = [
    #     'http://quotes.toscrape.com/page/1/',
    #     'http://quotes.toscrape.com/page/2/'
    # ]

#### Original parse to just get the entire page
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)

#### Parse to actually gather targeted info
    # def parse(self, response):
    #     for quote in response.css("div.quote"):
    #         yield {
    #             'text': quote.css("span.text::text").get(),
    #             'author': quote.css("small.author::text").get(),
    #             'tags': quote.css("div.tags a.tag::text").getall()
    #         }

    #     next_page = response.css("li.next a::attr(href)").get()
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page, callback=self.parse)

# MY SCRAPY STUFF
    def parse(self, response):
        paragraphs = response.xpath('//div[@class="article-content-body-only"]/p/text()').extract()
        return paragraphs

# response.xpath('//div[@class="article-content-body-only"]/p/text()').extract()