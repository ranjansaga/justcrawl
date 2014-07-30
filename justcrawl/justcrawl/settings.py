BOT_NAME = 'justcrawl'

SPIDER_MODULES = ['justcrawl.spiders']
NEWSPIDER_MODULE = 'justcrawl.spiders'

DEFAULT_ITEM_CLASS ='justcrawl.items.Website'
ITEM_PIPELINES = {'justcrawl.pipelines.FilterWordsPipeline': 0}
