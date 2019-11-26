import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def paytm_price(item_name):
    token1 = re.split(',|;|:|_| |\.', item_name)
    url = 'https://paytmmall.com/shop/search?q=' + \
        item_name+'&from=organic&child_site_id=6&site_id=2'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    box = soup.find_all('a', {"class": "_8vVO"})
    paytm_dict = {}
    i = 0
    for item in box:
        i = i+1
        if i>=6:
            break
        dict1 = {}
        newurl = "https://paytmmall.com/"+item['href']
        # dict1.update({"link":newurl})

        # newr=requests.get(newurl)
        # soup1=BeautifulSoup(newr.content,'html.parser')
        # print(soup1)
        img = item.find_all("img")[0]['src']
        # print(img)
        name1 = item.find_all("div", {"class": "UGUy"})

        price1 = item.find_all("div", {"class": "_1kMS"})
        flag = 0
        token2 = re.split(',|;|:|_| |\.', (name1[0].text).lower())
        #print(token2)
        for a in token1:
            if not a in token2:
                flag = 1
        if flag == 1:
            continue

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
        '''price_after_promo=soup1.find_all("div",{"class":"o1At"})
        if not len(price_after_promo)==0:
            print(price_after_promo[0].text[15:])
        promocode=soup1.find_all("div",{"class":"PF1t"})
        if not len(promocode)==0:
            print(promocode[0].text[11:]) 
        
        review=soup1.find_all("div",{"class":"_38Tb"})
        if not len(review)==0:
            print(review[0].text)
        
        warranty=soup1.find_all("div",{"class":"ZZBz nBgT"})
        if not len(warranty) ==0: 
            print(warranty[0].text)
         '''
    return paytm_dict
