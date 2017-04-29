# -*- coding: utf-8 -*-
__author__ = 'spacegoing'

import scrapy
from sogou_helpers import combo_names, \
    compete_url_list, coop_url_list
from urllib.parse import unquote


class MissingValueException(Exception):
    pass


class QuotesSpider(scrapy.Spider):
    name = "sougo"

    def start_requests(self):
        for url, names in zip(compete_url_list, combo_names):
            yield scrapy.Request(url=url, callback=self.parse,
                                 meta={'type': 'compete', 'names': names})
        for url, names in zip(coop_url_list, combo_names):
            yield scrapy.Request(url=url, callback=self.parse,
                                 meta={'type': 'cooperation', 'names': names})

    def parse(self, response):
        decode_names = [unquote(r) for r in response.meta['names']]
        try:
            resnum = response.css('resnum#scd_num::text').extract_first()

            # .extract_first() return `None` when nothing exists
            if not resnum:
                raise MissingValueException
            yield {'resnum': resnum, 'combo': decode_names, 'type': response.meta['type']}

        except MissingValueException:
            # Retry when missing values
            yield scrapy.Request(url=response.url, callback=self.parse,
                                 meta=response.meta, dont_filter=True)
