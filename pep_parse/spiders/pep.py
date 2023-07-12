import scrapy
from pep_parse.settings import SPIDER_NAME, DOMAINS_NAME, START_DOMAIN
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = SPIDER_NAME
    allowed_domains = DOMAINS_NAME
    start_urls = START_DOMAIN

    def parse(self, response):
        pep_hrefs = response.xpath(
            '//a[@class="pep reference internal"]/@href').getall()
        for link in pep_hrefs:
            link += '/'
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        data = {
            'number': title.split(' ')[1],
            'name': title.split('– ')[1],
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
