import scrapy
from datetime import date
class absenSpider(scrapy.Spider):
    name = 'absen'
    headers = {
        "X-Requested-With":"XMLHttpRequest"
    }
    dataAkun = {
        'user': '1914311005',
        'pass': 'U2FsdGVkX1/Vuw1aHMEpBHVFBZQKcE192YOCP37z4R4='
    }
    juduls = []
    links = []
    def start_requests(self):
        yield scrapy.FormRequest(
            url = 'http://sim.ubhara.ac.id/login/cek',
            headers = self.headers,
            formdata = self.dataAkun,
            callback = self.parse
        )

    def parse(self, response):
        yield scrapy.Request(
            url = 'http://sim.ubhara.ac.id/vclass',
            headers = self.headers,
            callback= self.listAbsen
        )
    
    def listAbsen(self,response):
        list = response.css('div.kt-portlet')


        for item in list:
            self.juduls.append(item.css("div.kt-widget__top > div:nth-child(3) > div > a::text").get().strip())
            self.links.append(item.css("div.kt-widget__bottom > div:nth-child(2) > div.kt-widget__details > a::attr(href)").get())


        for link in range(len(self.links)):
            yield scrapy.Request(
                url = f'http://sim.ubhara.ac.id{self.links[link]}',
                headers = self.headers,
                callback= self.checkAbsen,
                meta = {'link':f'http://sim.ubhara.ac.id{self.links[link]}'}
            )
    
    def checkAbsen(self,response):
        if response.css('#kt_content > div.kt-container.kt-grid__item.kt-grid__item--fluid > div.kt-widget14 > div > center > button'):
            yield{
                'Link Absen' : response.meta["link"],
                'Status Absen' : 'Ada',
                'Dicheck' : date.today().strftime("%B %d, %Y")
            }
        else:
            yield{
                'Link Absen' : response.meta["link"],
                'Status Absen' : 'Tidak Ada',
                'Dicheck' : date.today().strftime("%B %d, %Y")
            }
            