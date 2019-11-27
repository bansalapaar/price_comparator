"""
flipkart.py
================
This module is used to do webscraping on flikart website. It searches the product on the flipkart website entered by user and store the important information related to product
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def flipkart_price(item_name):
    """
    This function store the important information related to the searched product
	Parameters
	-----------------
	item_name is the name of the product entered by the user to be searched
	"""
    token1 = re.split(',|;|:|_| |\.', item_name)
    url ='https://www.flipkart.com/search?q='+item_name +'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&as-backfill=on'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    box = soup.find_all('a', {"class": "_31qSD5"})
    flipkart_dict = {}
    i = 0
    img = "https://st1.bgr.in/wp-content/uploads/2018/08/Flipkart-805px.jpg"
    box1 = soup.find_all('div', {"class": "IIdQZO _1R0K0g _1SSAGr"})
    """
    item on flipkart is present in three form so the following three condition are present to extract product information in any form
    """
    if not len(box) == 0:
        """
        This for loop iterates each item related to product on the flikart webpage and store information about it 
        """
        for item in box:
            i = i+1
            if i>=6:
                break
            dict1 = {}
            newurl = "https://www.flipkart.com"+item['href']
            #print(imgurl)
            # dict1.update({'link':newurl})
            name1 = item.find_all("div", {"class": "_3wU53n"})
            price1 = item.find_all("div", {"class": "_1vC4OE _2rQ-NK"})
            # review=soup1.find_all("span",{"class":"_38sUEc"})
            rating1 = item.find_all("div", {"class": "hGSR34"})
            # warranty=soup1.find_all("div",{"class":"_3LXPtT"})
            # color=soup1.find_all("div",{"class":"_11cw91 _1-fCbU E753YP DgCx9f"})
            # extra=soup1.find_all("li",{"class":"_2-n-Lg col"})
            # warranty=soup1.find_all("div",{"class":"_3h7IGd"})
            if not len(name1) == 0:
                dict1.update({"name": name1[0].text})
            else:
                dict1.update({"name":""})
            if not len(price1)==0:
                dict1.update({"price":int(price1[0].text[1:].replace(",",""))})
            else:
                dict1.update({"price":""})
            if not len(rating1)==0:
                dict1.update({"rating":rating1[0].text})
            else:
                dict1.update({"rating":""})
            dict1.update({"website":"Flipkart"})
            dict1.update({"url":newurl})
            dict1.update({"imgurl":img})  
            key="flip"+str(i)
            flipkart_dict.update({key:dict1})
    
    elif not len(box1)==0: 
    
       	"""
		This for loop iterates each item related to product on the flikart webpage and store information about it 
		"""
        i=0
        for item in box1:
            i=i+1
            if i>=6:
                break
            dict1={}
            # image_url=item.find_all('img',{"class":"_3togXc"})[0]['src']
            # print(image_url)
            new=item.find_all('a',{"class":"_2mylT6"})
            newurl="https://www.flipkart.com"+new[0]['href']
            # dict1.update({'link':newurl})
            name1=new[0]['title']#item.find_all("div",{"class":"_2mylT6"})
            price1=item.find_all("div",{"class":"_1vC4OE"})
            # review=soup1.find_all("span",{"class":"_38sUEc"})
            # rating1=box[k].find_all("div",{"class":"hGSR34"})
            # warranty=soup1.find_all("div",{"class":"_3LXPtT"})
            # color=soup1.find_all("div",{"class":"_11cw91 _1-fCbU E753YP DgCx9f"})
            # extra=soup1.find_all("li",{"class":"_2-n-Lg col"})
            # warranty=soup1.find_all("div",{"class":"_3h7IGd"})
            if not len(name1)==0:

                flag = 0
                dict1.update({"name":name1})
            else:
                dict1.update({"name":""})
            if not len(price1)==0:
                dict1.update({"price":int(price1[0].text[1:].replace(",",""))})
            else:
                dict1.update({"price":""})
            '''if not len(rating1)==0:
                dict1.update({"rating":rating1[0].text})'''
            dict1.update({"rating":"No rating"})
            dict1.update({"website":"Flipkart"})
            dict1.update({"url":newurl})  
            dict1.update({"imgurl":img})  
            key="flip"+str(i)
            flipkart_dict.update({key:dict1})
              

    else :
        box1=soup.find_all('div',{"class":"_3liAhj _1R0K0g"}) 

       	"""
		This for loop iterates each item related to product on the flikart webpage for webpage whose format does not match with above twoand store information about it 
		"""
        i=0
        for item in box1:
            i=i+1
            if i>=6:
                break
            dict1={}
            # image_url=item.find_all('img',{"class":"_3togXc"})[0]['src']
            # print(image_url)
            new=item.find_all('a',{"class":"_2cLu-l"})
            newurl="https://www.flipkart.com"+new[0]['href']
            # dict1.update({'link':newurl})
            name1=new[0]['title']#item.find_all("div",{"class":"_2mylT6"})
            price1=item.find_all("div",{"class":"_1vC4OE"})
            # review=soup1.find_all("span",{"class":"_38sUEc"})
            rating1=item.find_all("div",{"class":"hGSR34"})
            # warranty=soup1.find_all("div",{"class":"_3LXPtT"})
            # color=soup1.find_all("div",{"class":"_11cw91 _1-fCbU E753YP DgCx9f"})
            # extra=soup1.find_all("li",{"class":"_2-n-Lg col"})
            # warranty=soup1.find_all("div",{"class":"_3h7IGd"})
            if not len(name1)==0:
                flag = 0
                dict1.update({"name":name1})
            else:
                dict1.update({"name":""})
            if not len(price1)==0:
                dict1.update({"price":int(price1[0].text[1:].replace(",",""))})
            else:
                dict1.update({"price":""})
            if not len(rating1)==0:
                dict1.update({"rating":rating1[0].text})
            else:
                dict1.update({"rating":"No rating"})
                
            dict1.update({"website":"Flipkart"})
            dict1.update({"url":newurl})
            dict1.update({"imgurl":img})    
            key="flip"+str(i)
            flipkart_dict.update({key:dict1})
        print(flipkart_dict)    

    return flipkart_dict
