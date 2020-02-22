# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = [
        'https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc']

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths='//h3[@class="lister-item-header"]/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(
            restrict_xpaths='(//a[@class="lister-page-next next-page"])[2]'))
    )

    def parse_item(self, response):

        yield {
            'title': response.css('.title_wrapper > h1::text').get(),
            'year': response.css('.title_wrapper  #titleYear a::text').get(),
            'ratings': response.css('.ratingValue span[itemprop="ratingValue"]::text').get(),
            'genre': response.xpath('//div[@class = "subtext"]/a[@href][1]/text()').get(),
            'duration': response.css('.subtext time::text').get().strip(),
            'movie url': response.url}
