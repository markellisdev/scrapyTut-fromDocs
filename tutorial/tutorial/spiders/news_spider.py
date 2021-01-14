import scrapy
from scrapy.exporters import JsonLinesItemExporter
from tutorial.items import TutorialItem

# Scrapy Spider
class FinNewsSpider(scrapy.Spider):
    # Initializing log file
    # logfile("news_spider.log", maxBytes=1e6, backupCount=3)
    name = "news_spider"
    # allowed_domains = ['benzinga.com/']
    allowed_domains = ['marketwatch.com/']
    start_urls = [
        # 'https://www.benzinga.com/top-stories/20/09/17554548/stock-wars-ford-vs-general-motors-vs-tesla',
        'https://www.marketwatch.com/markets'
    ]

# MY SCRAPY STUFF
# response.xpath('//div[@class="article-content-body-only"]/p/text()').extract()
    def parse(self, response):
        # paragraphs = response.xpath('//div[@class="article-content-body-only"]/p/text()').extract()
        # print(paragraphs)
        # yield TutorialItem(content=paragraphs)
        ##### If I want to break up each p in a dict
        # for p in paragraphs:
        #     yield TutorialItem(content=p)
        headlines = response.xpath('//h3[@class="article__headline"]/a')
        for headline in headlines:
            print(headline.css("a::attr('href')").get())
            # yield {
            #     'link': headline.css("a::attr('href')").getall()
            # }
            #     'text': quote.css("span.text::text").get(),
            #     'author': quote.css("small.author::text").get(),
            #     'tags': quote.css("div.tags a.tag::text").getall()
            # }
# html.icons-loaded.enhanced body.page--peavey div.container.container--zone div.region.region--primary div.component.component--module.more-headlines.condensed div.column.column--primary.j-moreHeadlineWrapper div.collection__elements.j-scrollElement div.element.element--article.no-image div.article__content h3.article__headline
# /html/body/div[4]/div[2]/div[3]/div/div[1]/div[1]/div/h3/a