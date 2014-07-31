import scrapy
from scrapy.item import Item, Field
class Website(Item):
    date = Field()
    company = Field()
