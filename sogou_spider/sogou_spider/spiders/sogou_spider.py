# -*- coding: utf-8 -*-
__author__ = 'spacegoing'

import scrapy
from sogou_helpers import combo_names, \
    compete_url_list, coop_url_list
from urllib.parse import unquote


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
        resnum = response.css('resnum#scd_num::text').extract_first()
        decode_names = [unquote(r) for r in response.meta['names']]
        yield {'resnum': resnum, 'combo': decode_names, 'type': response.meta['type']}
