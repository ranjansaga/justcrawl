import scrapy
from scrapy.item import Item, Field
class Website(Item):
    name = Field()
    phone = Field()
