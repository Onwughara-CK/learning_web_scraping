# -*- coding: utf-8 -*-
import scrapy


class BestglassSpider(scrapy.Spider):
    name = 'bestglass'
    allowed_domains = ['glassesshop.com']
    start_urls = ['https://glassesshop.com/bestsellers']

    def parse(self, response):
        glasses = response.css('div.prlist .m-p-product')
        for glass in glasses:
            url = glass.css('.pimg a::attr(href)').get()
            if not url:  # prevent scraping ads
                continue
            img_url = glass.css(
                '.pimg a img.default-image-front::attr(src)').get()
            name = glass.css('div.row p.pname a::text').get()
            price = glass.css('div.row div.pprice span.pull-right::text').get()

            if not bool((price).strip()):  # if special price former price will be \n
                price = glass.css('div.row div.pprice span.sprice::text').get()

            yield {
                'url': url,
                'img_url': img_url,
                'name': name,
                'price': price
            }

        next_page = response.css(
            'div.custom-pagination li.page-item a[rel=\'next\']::attr(href)').get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
