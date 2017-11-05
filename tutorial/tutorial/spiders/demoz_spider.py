import scrapy


from tutorial.items import DmozItem

class DemzSpider(scrapy.Spider):
	name="dmoz"
	allowed_domains=['dmoztools.net']
	start_urls=['http://dmoztools.net/Reference/Bibliography/Science/'
	,"http://dmoztools.net/Reference/Bibliography/History/"
	]

	def parse(self,response):
		sel=scrapy.selector.Selector(response)
		sites=sel.xpath('//div[@class="title-and-desc"]')
		items=[]
		for site in sites:
			item=DmozItem()
			item['title']=site.xpath('a/div[@class="site-title"]/text()').extract()
			item['desc']=site.xpath('div/text()').extract()
			item['link']=site.xpath('a/@href').extract()
			items.append(item)

		return items



