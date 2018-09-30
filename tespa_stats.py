from scrapy import Request
from scrapy.spiders import Spider

class CollectTeams(Spider):
    name = 's2'

    #allowed_domains
    name = "s2"
    allowed_domains = ["tespa.org"]
    start_urls = ["https://compete.tespa.org/tournament/111/registrants?page={}".format(i) for i in range(1,24)]
    custom_settings = {
            'DOWNLOAD_DELAY': 0.3
           }

    def parse(self, response):
        names = response.xpath('//table/tbody/tr/td')
        ans=[]
        for name in names:
            item = {}
            item['team_name'] = name.xpath('a/text()').extract()
            item['team_link_url'] = name.xpath("a/@href").extract()
            if item['team_link_url']:
                req = Request((str(item['team_link_url'][0])), callback=self.parse_2)
                req.meta['foo'] = item
                ans.append(req)
        return ans

    def parse_2(self, response):
        it = response.meta['foo']
        btag = response.xpath('//div/table/tbody/tr/td[3]/text()').extract()
        #num_ratings = response.xpath('//section/div/div/div/h4/text()').extract()
        it['btag'] = btag
        return it       

