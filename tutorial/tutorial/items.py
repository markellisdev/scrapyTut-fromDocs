# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime

def remove_quotes(text):
    # strip unicode quotes
    text = text.strip(u'\u201c'u'\u201d')
    return text

def convert_date(text):
    # convert date string to Python date
    return datetime.strptime(text, '%B %d, %Y')


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    # pass

class QuoteItem(scrapy.Item):
    quote_content = Field(
        input_processor=MapCompose(remove_quotes),
        # TakeFirst to return first value, not whole list
        output_processor=TakeFirst()
    )
    tags = Field()
    author_name = Field()
    author_birthday = Field(
        input_processor=MapCompose(convert_date),
        output_processor=TakeFirst()
    )
    author_bornlocation = Field()
    author_bio = Field()
