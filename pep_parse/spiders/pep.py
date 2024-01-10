import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAIN, SPIDER_NAME, START_URL


class PepSpider(scrapy.Spider):
    name = SPIDER_NAME
    allowed_domains = ALLOWED_DOMAIN
    start_urls = START_URL

    def parse(self, response):
        tables = response.css('table.pep-zero-table.docutils.align-default')
        tr_tags = [table.css('tbody tr') for table in tables]
        for tr_tag_by_table in tr_tags:
            for tr_tag in tr_tag_by_table:
                pep_link = tr_tag.css('a::attr(href)').get()
                yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css('h1.page-title::text').get().split(' – ')
        number = number.replace('PEP ', '')
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
