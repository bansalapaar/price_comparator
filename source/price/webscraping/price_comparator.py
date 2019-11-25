from .amazon import amazon_price
from .flipkart import flipkart_price
from .paytm import paytm_price


class price_comp:
    def __init__(self):
        self.result=""
    def comp(self,item_name):
        amazon_dict = amazon_price(item_name)
    # print(amazon_dict)
    #print("paytm code")
        paytm_dict = paytm_price(item_name)
    #print("flipkart code")
        flipkart_dict = flipkart_price(item_name)

    # print(flipkart_dict)
    # print(paytm_dict)
        final_dict = {**flipkart_dict, **paytm_dict, **amazon_dict}
        #print(final_dict)

    # sort the items by price
        price_sort = sorted(final_dict.items(), key=lambda x: x[1]['price'])
        #print(price_sort)

    # sort the items by rating


        #rating_sort = sorted(final_dict.items(), key=lambda x: x[1]['rating'])     
        self.result=price_sort
        return (price_sort)
