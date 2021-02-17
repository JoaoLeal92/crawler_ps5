import scrapy
from crawlerPS5.items import Crawlerps5Item


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com.br']
    start_urls = [
        'https://www.amazon.com.br/PlayStation-Console-PlayStation%C2%AE5/dp/B088GNRX3J/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps5&qid=1613470308&sr=8-1',
        # Ulr below used for testing
        # 'https://www.amazon.com.br/God-War-Hits-PlayStation-4/dp/B07YT1GLV9/?_encoding=UTF8&pd_rd_w=yRrM3&pf_rd_p=d2ea4cd9-b3fa-4bdb-ab83-24ca9c54ecbe&pf_rd_r=3JF03Z0NMXW0PXVM86Z1&pd_rd_r=b592df2f-51e0-4fe5-8ccd-e6ff9930134e&pd_rd_wg=CLvfl&ref_=pd_gw_ci_mcx_mr_hp_d'
    ]

    def parse(self, response):
        product_title = response.xpath('//span[@id="productTitle"]/text()').get()
        if product_title:
            product_title = product_title.strip()

        product_price = response.xpath('//span[@id="priceblock_ourprice"]/text()').get()

        ps5 = Crawlerps5Item(name=product_title, price=product_price)
        yield ps5
