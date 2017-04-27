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
            yield scrapy.Request(url=url, callback=self.parse_compete,
                                 meta={'comb_name': names})
        for url, names in zip(coop_url_list, combo_names):
            yield scrapy.Request(url=url, callback=self.parse_coop,
                                 meta={'comb_name': names})

    def parse_compete(self, response):
        resnum = response.css('resnum#scd_num::text').extract_first()
        decode_names = [unquote(r) for r in response.meta['comb_name']]
        yield {'resnum': resnum, 'combo': decode_names, 'type': '竞争'}

    def parse_coop(self, response):
        resnum = response.css('resnum#scd_num::text').extract_first()
        decode_names = [unquote(r) for r in response.meta['comb_name']]
        yield {'resnum': resnum, 'combo': decode_names, 'type': '合作'}
