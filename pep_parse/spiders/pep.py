import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_hrefs = response.xpath(
            '//a[@class="pep reference internal"]/@href').getall()
        for link in pep_hrefs:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        data = {
            'number': title.split(' ')[1],
            'name': title.split('– ')[1],
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
