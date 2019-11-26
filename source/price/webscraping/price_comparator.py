from .amazon import amazon_price
from .flipkart import flipkart_price
from .paytm import paytm_price
from .snapdeal import snapdeal_price
#from best import paytmbest,flikartbest,amazonbest


class price_comp:
    def __init__(self):
        self.result=""
    def comp(self,item_name):
        dict1={}
        item_name=item_name.lower()
        amazon_dict ={}#amazon_price(item_name)
        #if 'amazon1' in amazon_dict:
        #    dict1.update({'amazon':amazon_dict['amazon1']})

        paytm_dict =paytm_price(item_name)
        dict1.update({'paytm':paytm_dict['paytm1']})

        flipkart_dict =flipkart_price(item_name)
        dict1.update({'flipkart':flipkart_dict['flip1']})
        snapdeal_dict =snapdeal_price(item_name)
        dict1.update({'snapdeal':snapdeal_dict['snapdeal1']})
        final_dict = {**flipkart_dict, **paytm_dict, **amazon_dict,**snapdeal_dict}
        #print(final_dict)

    # sort the items by price
        price_sort = sorted(final_dict.items(), key=lambda x: x[1]['price'])
        for a in dict1:
            price_sort.insert(0,(a,dict1[a]))
        #print(price_sort)
        self.result=price_sort
        return (price_sort)
