"""
price_comparator.py
======================
This is the main program which call the function from amazon.py, flipkart.py, paytm.py and snapdeal.py to extract information from all the websites and integrate them into single list of items according to best deal. 
"""
from .amazon import amazon_price
from .flipkart import flipkart_price
from .paytm import paytm_price
from .snapdeal import snapdeal_price
#from best import paytmbest,flikartbest,amazonbest


class price_comp:
    def __init__(self):
        """
        it initialise the result list with null.
        """
        self.result=""

    def comp(self,item_name):
        dict1=[]
        item_name=item_name.lower()
        amazon_dict =amazon_price(item_name)
        if 'amazon1' in amazon_dict:
            print("amazon worked")
            dict1.append(('amazon',amazon_dict['amazon1']))
            del(amazon_dict['amazon1'])
        """
        this

        parameter
        -----------------
        it take item_name as input parameter and passes this item to all the functions (amazon_price,flipkart_price,paytm_price,snapdeal_price)
        and sort them item according to the lowest price.
        """
        paytm_dict =paytm_price(item_name)
        dict1.append(('paytm',paytm_dict['paytm1']))
        del(paytm_dict['paytm1'])

        flipkart_dict =flipkart_price(item_name)
        dict1.append(('flipkart',flipkart_dict['flip1']))
        del(flipkart_dict['flip1'])
        snapdeal_dict =snapdeal_price(item_name)
        dict1.append(('snapdeal',snapdeal_dict['snapdeal1']))
        del(snapdeal_dict['snapdeal1'])
        final_dict = {**flipkart_dict, **paytm_dict, **amazon_dict,**snapdeal_dict}
        #print(final_dict)

    # sort the items by price
        price_sort = sorted(final_dict.items(), key=lambda x: x[1]['price'])
        price_sort=[('first',dict1),('second',price_sort)]
        #for a in dict1:
            #price_sort.insert(0,(a,dict1[a]))
        #print(price_sort)
        #print(price_sort[0])
        self.result=price_sort
        return (price_sort)
