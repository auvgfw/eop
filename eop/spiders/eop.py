import scrapy


class QuotesSpider(scrapy.Spider):
    name = "eop"

    def start_requests(self):
        urls=[]
        for i in range(1,1216):
            url='https://www.everyonepiano.cn/Music.html?&p=' + str(i)
            urls.append(url)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for MusicIndexBox in response.css('div.MusicIndexBox'):
            MITitle=MusicIndexBox.css('div.MITitle')
            yield {
                'MITitle': MusicIndexBox.css(' div.MITitle a::attr(href)').extract_first(),
            }
if __name__ == '__main__':
    print("start")

