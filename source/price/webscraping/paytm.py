"""
paytm.py
================
This module is used to do webscraping on paytm mall website. It searches the product on the paytm mall website entered by user and store the important information related to product
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def paytm_price(item_name):
    
    """
    This function store the important information related to the searched product
    Parameters
    -----------------
    item_name is the name of the product entered by the user to be searched
    """
    token1 = re.split(',|;|:|_| |\.', item_name)
    url = 'https://paytmmall.com/shop/search?q=' + \
        item_name+'&from=organic&child_site_id=6&site_id=2'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    box = soup.find_all('a', {"class": "_8vVO"})
    paytm_dict = {}
    i = 0
    for item in box:
        """
        This for loop iterates each item related to product on the paytm mall webpage and store information about it. 
        """
        i = i+1
        if i>=6:
            break
        dict1 = {}
        newurl = "https://paytmmall.com/"+item['href']
 
        img = item.find_all("img")[0]['src']
 
        name1 = item.find_all("div", {"class": "UGUy"})

        price1 = item.find_all("div", {"class": "_1kMS"})
        dict1.update({"name": name1[0].text})
        dict1.update({"price": int(price1[0].text.replace(",", ""))})
        rating1 = item.find_all("div", {"class":"_2MEo"})
        if not len(rating1) == 0:
            dict1.update({"rating": rating1[0].text})
        else:
            dict1.update({"rating": "No ratings found"})

        dict1.update({"website": "Paytm Mall"})
        dict1.update({"url": newurl})
        dict1.update({"imgurl": img})
        key = "paytm"+str(i)
        paytm_dict.update({key: dict1})

    return paytm_dict
