from typing import Text
import scrapy
from scrapy import loader
from scrapy.exporters import JsonLinesItemExporter
from scrapy.loader import ItemLoader
from tutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"

#### Actually don't have to use the start_requests function since it's built in. Can just use start_urls
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/'
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    start_urls = [
        'http://quotes.toscrape.com'
    ]

#### Original parse to just get the entire page
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)

#### Parse to actually gather targeted info
    def parse(self, response):
        self.logger.info('Parse function called on {}'.format(response.url))
        quotes = response.css("div.quote")
        for quote in quotes:
            # yield {
            #     'text': quote.css("span.text::text").get(),
            #     'author': quote.css("small.author::text").get(),
            #     'tags': quote.css("div.tags a.tag::text").getall()
            # }
            # replaced the above with this item loader
            loader = ItemLoader(item=QuoteItem(), selector=quote)
            loader.add_css('quote_content', '.text::text')
            loader.add_css('tags', '.tag::text')
            quote_item = loader.load_item() # end of item loader

            author_url = quote.css('.author + a::attr(href)').get()
            self.logger.info('get author page url')
            # go to the author page
            yield response.follow(author_url, callback=self.parse_author, meta={'quote_item': quote_item})

        # next_page = response.css("li.next a::attr(href)").get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

        # Replaced the above with........
        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)
    
    def parse_author(self, response):
        quote_item = response.meta['quote_item']
        loader = ItemLoader(item=quote_item, response=response)
        loader.add_css('author_name', '.author-title::text')
        loader.add_css('author_birthday', '.author-born-date::text')
        loader.add_css('author_bornlocation', '.author-born-location::text')
        loader.add_css('author_bio', '.author-description::text')
        yield loader.load_item()
        # yield {
        #     'quote_item': response.meta['quote_item'],
        #     'author_name': response.css('.author-title::text').get(),
        #     'author_birthday': response.css('.author-born-date::text').get(),
        #     'author_bornlocation': response.css('.author-born-location::text').get(),
        #     'author_bio': response.css('.author-description::text').get()
        # }