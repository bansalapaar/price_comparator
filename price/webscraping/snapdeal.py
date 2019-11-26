import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def snapdeal_price(item_name):
    token1 = re.split(',|;|:|_| |\.', item_name)
    url = 'https://www.snapdeal.com/search?keyword='+"+".join(token1)+'&sort=rlvncy'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    box = soup.find_all('div', {"class": "col-xs-6"})
    snapdeal_dict = {}
    i = 0
    for item in box:
        #print(item)
        i = i+1
        if i>5:
            break
        dict1 = {}
        #print(item)
        newurl=item.find_all('a',attrs={'class':'dp-widget-link'})
        dict1.update({"link":newurl[0]['href']})
        imga=item.find('picture',attrs={'class':'picture-elem'})
        imgurl=imga.find("img")
        imgurl1=[]
        #print(imgurl)
        try:
            imgurl1=re.split("\n",imgurl['src'])
            dict1.update({'imgurl':imgurl1})
            print(imgurl1)
        except:
            imgurl1=re.split("\n",imgurl['data-src'])
            dict1.update({'imgurl':imgurl1})
            print(imgurl1)
        dict1.update({'imgurl':imgurl1})
        name=imgurl['title']
        token2 = re.split(',|;|:|_| |\.', (name).lower())
        #print(token2)
        flag=0
        for a in token1:
            if not a in token2:
                flag = 1
        if flag == 1:
            i-=1
            continue
        dict1.update({'name':name})
        price=item.find('span',attrs={'class':'lfloat product-price'})['display-price']
        dict1.update({'price':int(price)})
        print(price)
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