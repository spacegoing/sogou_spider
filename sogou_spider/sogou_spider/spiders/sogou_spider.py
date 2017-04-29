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
        decode_names = [unquote(r).strip('"') for r in response.meta['names']]
        resnum = response.css('resnum#scd_num::text').extract_first()

        # .extract_first() return `None` when nothing exists
        # sogou doesn't display resnum when results < 1 page
        if not resnum:
            resnum = len(response.css('div.results').xpath('div'))
            self.logger.info('Less than 1 page on query: "%s"+AND+"%s"+AND+"%s"' % (decode_names[0], decode_names[1],
                                                                      response.meta['type']))

        yield {'resnum': resnum, 'combo': decode_names, 'type': response.meta['type']}
