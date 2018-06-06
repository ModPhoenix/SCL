# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import MapCompose, TakeFirst

from knowledgebase.models import ShipItem

class MyItemLoader(XPathItemLoader):
    default_item_class = ShipItem
    default_input_processor = MapCompose(lambda string: string.strip())
    default_output_processor = TakeFirst()

class ShipSpider(scrapy.Spider):
    name = 'Ship'

    custom_settings = {
        'ITEM_PIPELINES': {
            'knowledgebase.pipelines.ShipPipeline': 300,
        }
    }

    allowed_domains = ['starcitizen.tools']
    start_urls = ['https://starcitizen.tools/Category:Ships']

    def parse(self, response):

        for ship_url in response.xpath("//tr/td[1]/a/attribute::href").extract():
            yield scrapy.Request(response.urljoin(ship_url), callback=self.parse_ship_page)

    def parse_ship_page(self, response):
        l = MyItemLoader(response=response)
        l.add_xpath('name', '//h1[@id="firstHeading"]/text()')
        l.add_xpath('focus', '//td[text() = "Focus"]/following-sibling::*/text()')
        l.add_xpath('prod_state', '//td[text() = "Production State"]/following-sibling::*/text()')
        l.add_xpath('max_crew', '//td[text() = "Maximum Crew"]/following-sibling::*/text()')
        l.add_xpath('cargo_capacity', '//td[text() = "Cargo Capacity"]/following-sibling::*/text()')
        l.add_xpath('rec_cost', '//td[text() = "REC Cost"]/following-sibling::*/text()')
        l.add_xpath('pledge_cost', '//td[text() = "Pledge Cost"]/following-sibling::*/text()')
        l.add_xpath('null_cargo_mass', '//td[text() = "Null-cargo Mass"]/following-sibling::*/text()')
        l.add_xpath('length', '//td[text() = "Length"]/following-sibling::*/text()')
        l.add_xpath('height', '//td[text() = "Height"]/following-sibling::*/text()')
        l.add_xpath('beam', '//td[text() = "Beam"]/following-sibling::*/text()')
        return l.load_item()
