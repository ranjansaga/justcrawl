from scrapy.exceptions import DropItem

class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""
    
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            return item
