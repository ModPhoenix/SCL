# -*- coding: utf-8 -*-
import scrapy
import json
from database.models import FundingItem


class FundingSpider(scrapy.Spider):
    name = 'funding'
    allowed_domains = ['robertsspaceindustries.com']
    start_urls = ['http://robertsspaceindustries.com/']

    def start_requests(self):
        data = {'fans': 'true', 'funds': 'true', 'fleet': 'true'}
        request_body = json.dumps(data)
        yield scrapy.Request('https://robertsspaceindustries.com/api/stats/getCrowdfundStats',
                             method="POST",
                             body=request_body,
                             headers={
                                 'Content-Type': 'application/json; charset=UTF-8'},
                             callback=self.parse_funding)

    def parse_funding(self, response):
        item = FundingItem()
        jsonresponse = json.loads(response.body_as_unicode())
        item["success"] = jsonresponse["success"]
        item["fans"] = jsonresponse["data"]["fans"]
        item["funds"] = jsonresponse["data"]["funds"]

        yield item
