# -*- coding: utf-8 -*-
import scrapy


class D2gSpider(scrapy.Spider):
    name = 'd2g'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = [
        'http://worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response):
        rows = response.css('tbody tr')
        for row in rows:
            country_name = row.css('td a::text').get()
            gdp_debt = row.css('td::text')[0].get()

            try:
                population = row.css('td::text')[1].get()
            except:
                population = None

            yield {
                'country_name': country_name,
                'gdp_dept': gdp_debt,
                'population': population
            }
