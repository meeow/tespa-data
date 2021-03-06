from scrapy import Request
from scrapy.spiders import Spider
import datetime

class CollectTeams(Spider):
    name = 's2'

    #allowed_domains
    name = "s2"
    allowed_domains = ["tespa.org"]
    start_urls = ["https://compete.tespa.org/tournament/111/leaderboard"]
    custom_settings = {
            'DOWNLOAD_DELAY': 0.3
           }

    def parse(self, response):
        names = response.xpath("//table/tbody/tr")
        ans=[]
        for name in names:
            #print (name)
            item = {}
            item['rank'] = name.xpath('td[1]/text()').extract()
            item['team_name'] = name.xpath("td/a/span/text()").extract()
            item['rating'] = name.xpath("td[3]/text()").extract()
            item['timestamp'] = datetime.datetime.now()
            ans.append(item)
        return ans

 

