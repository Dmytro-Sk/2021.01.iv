class Locators:

    """Page 1"""
    
    # main locators

    # additional locators
    DATA = '//script[@class="GTM-activeFilters"]/text()'
    PAGES_AMOUNT = '//div[@class="row product-lists"]/div[last()]//li[last()-1]/a/text()'

    """Page 2"""

    # main locators
    ITEM_DATA = '//div[@data-widget="datalayer/product_detail"]/script/text()'
    IMAGE_URL = '//div[@class="detail"]//div[@class="row"]//a/@href'
    BRAND = '//div[@class="detail"]//div[@class="row"]/div[2]/div/div/text()'
    PRICE = '//span[@class="product__prices-sale"]/text()'
    TITLE = '//div[@class="detail"]//div[@class="row"]/div[2]//h1/text()'
    DESCRIPTION = '//div[@class="detail"]//div[@class="row"]/div[2]//div[@class="detail__description-content"]//text()'
    GENDER = '//div[@class="detail"]//div[@class="row"]/div[2]//div[@class="row detail__properties"]/div[3]/div/div[2]//text()'

    # additional locators
    CATEGORY = '//div[@class="breadcrumb"]/a[2]/text()'
    SUBCATEGORY_LVL1 = '//div[@class="breadcrumb"]/a[3]/text()'
    SUBCATEGORY_LVL2 = '//div[@class="breadcrumb"]/a[4]/text()'
