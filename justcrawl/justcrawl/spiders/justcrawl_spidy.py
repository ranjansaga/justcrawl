from scrapy.spider import Spider
from scrapy.selector import Selector
from justcrawl.items import Website


class JustCrawlSpider(Spider):
    name = "justdial"
    allowed_domains = ["justdial.com"]
    start_urls = [
        "http://www.justdial.com/Bangalore/Plumbers/ct-134859/page-1",
        "http://www.justdial.com/Bangalore/Plumbers/ct-134859/page-2",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath("//*/section[@class='rslwrp']/section/section[2]/section/aside[@class='compdt']")
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.xpath("p/span[@class='jcn']/a/@title").extract()
            item['phone'] = site.xpath("p[@class='jrcw']/a/@href").extract()
            items.append(item)

        return items
