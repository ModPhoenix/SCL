# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from django.template.defaultfilters import slugify

class DatabasePipeline(object):

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




        # print('Проверка slug =', item['slug'])
        # print('Проверка focus =', item['focus'])
        # print('Проверка prod_state =', item['prod_state'])
        # print('Проверка max_crew =', item['max_crew'])
        # #item["rec_cost"] = str(re.sub("\D", "", item["rec_cost"]))
        # print('Проверка rec_cost =', item['rec_cost'])
        # item["pledge_cost"] = str(re.sub("\D", "", item["pledge_cost"]))
        # print('Проверка pledge_cost =', item['pledge_cost'])
        # item["cargo_capacity"] = str(re.sub("\D", "", item["cargo_capacity"]))
        # item["null_cargo_mass"] = str(re.sub("\D", "", item["null_cargo_mass"]))

        # item["length"] = item["length"].split(' ')[0]
        # item["height"] = item["height"].split(' ')[0]
        # item["beam"] = item["beam"].split(' ')[0]
        item.save()

        return item