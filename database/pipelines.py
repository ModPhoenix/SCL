# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from django.template.defaultfilters import slugify


class ShipPipeline(object):

    def process_item(self, item, spider):

        item['slug'] = slugify(item["name"])

        if "cargo_capacity" in item:
            item["cargo_capacity"] = re.sub("\D", "", item["cargo_capacity"])

        if "rec_cost" in item:
            item["rec_cost"] = re.sub("\D", "", item["rec_cost"])

        if "pledge_cost" in item:
            item["pledge_cost"] = re.sub("\D", "", item["pledge_cost"])

        if "null_cargo_mass" in item:
            item["null_cargo_mass"] = re.sub("\D", "", item["null_cargo_mass"])

        if "length" in item:
            item["length"] = item["length"].split(' ')[0]

        if "height" in item:
            item["height"] = item["height"].split(' ')[0]

        if "beam" in item:
            item["beam"] = item["beam"].split(' ')[0]

        item.save()

        return item

class CompanyPipeline(object):

    def process_item(self, item, spider):

        item['slug'] = slugify(item["name"])

        item.save()

        return item