"""
snapdeal.py
================
This module is used to do webscraping on snapdeal website. It searches the product on the sandeal website entered by user and store the important information related to product
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def snapdeal_price(item_name):
    """
    This function store the important information related to the searched product
    Parameters
    -----------------
    item_name is the name of the product entered by the user to be searched
    """
    token1 = re.split(',|;|:|_| |\.', item_name)
    url = 'https://www.snapdeal.com/search?keyword='+"+".join(token1)+'&sort=rlvncy'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    box = soup.find_all('div', {"class": "col-xs-6"})
    snapdeal_dict = {}
    i = 0
    for item in box:
        """
        This for loop iterates each item related to product on the snapdeal webpage and store information about it 
        """
        i = i+1
        if i>5:
            break
        dict1 = {}
        #dictionary to store the information about the item dataset
        newurl=item.find('a',attrs={'class':'dp-widget-link'})
        if not newurl==None:
            dict1.update({"link":newurl['href']})
        else:
            dict1.update({"link":url})
        imga=item.find('picture',attrs={'class':'picture-elem'})
        imgurl=imga.find("img")
        imgurl1=[]
        #print(imgurl)
        try:
            imgurl1=re.split("\n",imgurl['src'])
            dict1.update({'imgurl':imgurl1[0]})
            #print(imgurl1[0])
        except:
            imgurl1=re.split("\n",imgurl['data-src'])
            dict1.update({'imgurl':imgurl1[0][:]})
            #print(imgurl1[0][:])
        dict1.update({'imgurl':imgurl1[0][:]})
        name=imgurl['title']
        dict1.update({'name':name})
        price=item.find('span',attrs={'class':'lfloat product-price'})['display-price']
        dict1.update({'price':int(price)})
        #print(price)
        rating=item.findAll('div',attrs={'class':'filled-stars'})
        if 'style' in rating:
            rat=rating['style'][6:-1]/20
            dict1.update({'rating':rat})
        else:
            dict1.update({'rating':"No rating found"})
        s="snapdeal"+str(i)
        dict1.update({'website':'Snapdeal'})
        snapdeal_dict.update({s:dict1})
    #print(snapdeal_dict)
    return snapdeal_dict
