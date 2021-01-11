# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    # pass

class QuoteItem(scrapy.Item):
    quote_content = Field()
    tags = Field()
    author_name = Field()
    author_birthday = Field()
    author_bornlocation = Field()
    author_bio = Field()
    