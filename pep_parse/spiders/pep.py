import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        links = response.css('a[class^="pep"]::attr(href)').getall()
        for link in links:
            yield response.follow(link, self.parse_pep)

    def parse_pep(self, response):
        number_and_name = response.css(
            'h1.page-title::text'
        ).get().replace('PEP', '').split('–')
        data = {
            'number': int(number_and_name[0].strip()),
            'name': number_and_name[1].strip(),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }
        yield PepParseItem(data)
