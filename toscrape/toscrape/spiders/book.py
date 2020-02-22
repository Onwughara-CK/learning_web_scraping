# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/index.html']

    rules = (
        Rule(LinkExtractor(restrict_css='.image_container a'),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_css='li.next a'))
    )

    def parse_item(self, response):
        yield {
            'title': response.css('.product_main h1::text').get(),
            'price': response.css('.product_main .price_color::text').get()
        }
