from scrapy.spider import Spider
from scrapy.selector import Selector
from justcrawl.items import Website


class JustCrawlSpider(Spider):
    name = "jobdetails"
    allowed_domains = ["allindiajobs.com"]
    start_urls = [
                   "http://www.allindiajobs.in/"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath(".//*/div[@class='post h-entry']")
        items = []

        for site in sites:
            item = Website()
            item['company'] = site.xpath("h2/a/text()").extract()
            item['date'] = site.xpath("div[2]/div[2]/b/span/text()").extract()
            items.append(item)

        return items

