# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import MapCompose, TakeFirst

from knowledgebase.models import CompanyItem

class MyItemLoader(XPathItemLoader):
    default_item_class = CompanyItem
    default_input_processor = MapCompose(lambda string: string.strip())
    default_output_processor = TakeFirst()

class ShipSpider(scrapy.Spider):
    name = 'Company'

    custom_settings = {
        'ITEM_PIPELINES': {
            'knowledgebase.pipelines.CompanyPipeline': 300,
        }
    }

    allowed_domains = ['starcitizen.tools']
    start_urls = ['https://starcitizen.tools/Category:Companies']

    def parse(self, response):

        for company_url in response.xpath("//div[@class='mw-category']/div/ul/li/a/attribute::href").extract():
            yield scrapy.Request(response.urljoin(company_url), callback=self.parse_company_page)


    def parse_company_page(self, response):
        l = MyItemLoader(response=response)
        l.add_xpath('name', '//h1[@id="firstHeading"]/text()')
        l.add_xpath('industry', '//td[text() = "Industry"]/following-sibling::*/text()')
        l.add_xpath('race', '//td[text() = "Race"]/following-sibling::*/text()')
        l.add_xpath('code', '//td[text() = "Manufacturer Code"]/following-sibling::*/text()')
        l.add_xpath('current_ceo', '//td[text() = "Current CEO"]/following-sibling::*/text()')
        l.add_xpath('founder', '//td[text() = "Founder"]/following-sibling::*/a/text()')
        l.add_xpath('founded', '//td[text() = "Founded"]/following-sibling::*/text()')
        l.add_xpath('demographic', '//td[text() = "Demographic"]/following-sibling::*/text()')
        return l.load_item()
