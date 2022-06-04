import scrapy


class TwittersearchSpider(scrapy.Spider):
    name = 'twittersearch'
    headers = {
            "User-Agent": "v2RecentSearchJS",
            "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAACHudAEAAAAAiE%2Fyuze7bbllbOH1QOUyPSiL3T0%3DNlTn4xjGBG8Qvqg3OBlg0XcSTYfjpS0nA8lSh1bbUDKFaTsxJm"
        }

    def start_requests(self):
        yield scrapy.Request(
            url = 'https://api.twitter.com/2/tweets/search/recent?query=ubhara&max_results=100&tweet.fields=created_at',
            headers = self.headers,
            callback = self.parse
        )

    def parse(self, response):
        datanya = response.json()
        for data in datanya['data']:
            yield{
                'id' : data['id'],
                'text' : data['text'],
                'created_at' : data['created_at']
            }
