# -*- coding: utf-8 -*-
import scrapy
import json


class ShipSpider(scrapy.Spider):
    name = 'Ship'
    allowed_domains = ['starcitizen.tools']
    start_urls = ['https://starcitizen.tools/Category:Ships']
    print('Start')

    def parse(self, response):
        for ship_url in response.xpath("//tr/td[1]/a/attribute::href").extract():
            yield scrapy.Request(response.urljoin(ship_url), callback=self.parse_ship_page)

    def parse_ship_page(self, response):
        item = {}
        item["name"] = response.xpath("//th[@class='infobox-table-name fn']/text()").extract()
        item["focus"] = response.xpath("//td[text() = 'Focus']/following-sibling::*/text()").extract()
        item["prod_state"] = response.xpath("//td[text() = 'Production State']/following-sibling::*/text()").extract()
        item["max_crew"] = response.xpath("//td[text() = 'Maximum Crew']/following-sibling::*/text()").extract()
        item["rec_cost"] = response.xpath("//td[text() = 'REC Cost']/following-sibling::*/text()").extract()
        item["pledge_cost"] = response.xpath("//td[text() = 'Pledge Cost']/following-sibling::*/text()").extract()
        item["cargo_capacity"] = response.xpath("//td[text() = 'Cargo Capacity']/following-sibling::*/text()").extract()
        item["null_cargo_mass"] = response.xpath("//td[text() = 'Null-cargo Mass']/following-sibling::*/text()").extract()
        item["length"] = response.xpath("//td[text() = 'Length']/following-sibling::*/text()").extract()
        item["height"] = response.xpath("//td[text() = 'Height']/following-sibling::*/text()").extract()

        yield item
