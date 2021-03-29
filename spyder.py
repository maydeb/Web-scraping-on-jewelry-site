import scrapy
import math

class JewelrySpider(scrapy.Spider):
    name= 'jewelry'

    start_urls=['https://www.houseofindya.com/zyra/cat?page=1']                                     #starting page for jewelry

    def parse(self, response):

        total_products= int((response.css('.totalRecords::text').extract())[0])                     #total no. of products
                                                                                
        number_of_pages= math.ceil(total_products/products_per_page)                                #total no. of pages

        products=response.css('ul#JsonProductList')
        products=products.css('li')                                             #list of product attributes
        products_per_page=len(prodcuts)                                            #no. of products per page



        for product in products:
            id=product.attrib['data-variants']                                                      #unique product id
            yield{
                'product_desc': product.attrib['data-name'],
                'price': product.attrib['data-price'],
                'image': "https://img.faballey.com/Images/Product/%s/1.jpg" %id ,
                'link': product.attrib['data-url'],



                    }

        for page in range(2,number_of_pages+1):                                                       #traversing through pages
            url = 'https://www.houseofindya.com/zyra/cat?page={}'.format(page)
            yield response.follow(url, callback=self.parse)


