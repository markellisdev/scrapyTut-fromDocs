# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
# from scrapy.loader.processors import MapCompose, TakeFirst --- since tutorial, these had been deprecated
from itemloaders.processors import MapCompose, TakeFirst
from datetime import datetime

def remove_quotes(text):
    # strip unicode quotes
    text = text.strip(u'\u201c'u'\u201d')
    return text

def convert_date(text):
    # convert date string to Python date
    return datetime.strptime(text, '%B %d, %Y')

def parse_location(text):
    # parse location "in Ulm, Germany"
    # this removes "in" by slicing and keeping everything from 3rd charcter on [3:]. Can further parse city, state, country if desired
    return text[3:]


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = Field()
    link = Field()
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
    author_bornlocation = Field(
        input_processor=MapCompose(parse_location),
        output_processor=TakeFirst()
    )
    author_bio = Field()
