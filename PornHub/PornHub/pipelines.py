# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class PornhubMongoDBPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("192.168.71.178", 27017)
        db = clinet["PornHub"]
        self.PhRes = db["PhRes"]

    def process_item(self, item, spider):
        print('MongoDBItem', item)
        """ 判断类型 存入MongoDB """
        from spy.WebHubBot.PornHub.PornHub.items import PornVideoItem
        if isinstance(item, PornVideoItem):
            print('PornVideoItem True')
            try:
                self.PhRes.insert(dict(item))
            except Exception:
                pass
        return item
