import scrapy
from scrapy_selenium import SeleniumRequest
import time
class NgambilreviewSpider(scrapy.Spider):
    name = 'ngambilreview'
    def start_requests(self):
        yield SeleniumRequest(
            url ="https://www.google.com/maps/place/Bhayangkara+University+of+Surabaya/@-7.3213728,112.7320547,15z/data=!4m7!3m6!1s0x0:0xfb373fa4ca06ffd2!8m2!3d-7.3213728!4d112.7320547!9m1!1b1",
            wait_time= 3,
            screenshot = True,
            callback = self.parse, 
            dont_filter = True 
        )
  
    def parse(self, response):
        hasil = response.selector.css("div.jJc9Ad")
        for x in hasil:
            # gambar
            img = x.css("img.NBa7we")
            # nama
            nama = x.css("div.d4r55 span::text")
            # bintang
            bintang = x.css("span.kvMYJc")
            # waktu
            waktu = x.css("span.rsqaWe::text")
            # isinya
            isinya = x.css("span.wiI7pd::text")
            yield{
                'Gambar' : img.attrib['src'],
                'Nama' : nama.get(),
                'Bintang' : bintang.attrib['aria-label'],
                'Waktu' : waktu.get(),
                'Isinya' : isinya.get(),
            }
    