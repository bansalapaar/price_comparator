import requests
from bs4 import BeautifulSoup
import pandas as pd
def flipkart_price(item_name):
    url='https://www.flipkart.com/search?q='+item_name+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&as-backfill=on'
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    box=soup.find_all('a',{"class":"_31qSD5"})
    flipkart_dict={}
    i=0
    img=""
    box1=soup.find_all('div',{"class":"IIdQZO _1R0K0g _1SSAGr"}) 
    if not len(box)==0:
        for item in box:
            i=i+1
            dict1={}
            newurl="https://www.flipkart.com"+item['href']
            #dict1.update({'link':newurl})
            name1=item.find_all("div",{"class":"_3wU53n"})
            price1=item.find_all("div",{"class":"_1vC4OE _2rQ-NK"})
            #review=soup1.find_all("span",{"class":"_38sUEc"})
            rating1=item.find_all("div",{"class":"hGSR34"})
            #warranty=soup1.find_all("div",{"class":"_3LXPtT"})
            #color=soup1.find_all("div",{"class":"_11cw91 _1-fCbU E753YP DgCx9f"})
            #extra=soup1.find_all("li",{"class":"_2-n-Lg col"})
            #warranty=soup1.find_all("div",{"class":"_3h7IGd"})
            if not len(name1)==0:
                dict1.update({"name":name1[0].text})
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
        #print(review[0].text)
            #,"\t\t",rating[0].text,"\t\t")
        '''for a in color:
            print(a.text)
        for a in warranty:
            print(a.text)
        for a in extra:
            print(a.text)'''
    elif not len(box1)==0: 
        #box1=soup.find_all('div',{"class":"_2LFGJH"})
        #print(box)
        for item in box1:
            i=i+1
            dict1={}
            #image_url=item.find_all('img',{"class":"_3togXc"})[0]['src']
            #print(image_url)
            new=item.find_all('a',{"class":"_2mylT6"})
            newurl="https://www.flipkart.com"+new[0]['href']
            #dict1.update({'link':newurl})
            name1=new[0]['title']#item.find_all("div",{"class":"_2mylT6"})
            price1=item.find_all("div",{"class":"_1vC4OE"})
            #review=soup1.find_all("span",{"class":"_38sUEc"})
            #rating1=box[k].find_all("div",{"class":"hGSR34"})
            #warranty=soup1.find_all("div",{"class":"_3LXPtT"})
            #color=soup1.find_all("div",{"class":"_11cw91 _1-fCbU E753YP DgCx9f"})
            #extra=soup1.find_all("li",{"class":"_2-n-Lg col"})
            #warranty=soup1.find_all("div",{"class":"_3h7IGd"})
            if not len(name1)==0:
                dict1.update({"name":name1})
            else:
                dict1.update({"name":""})
            if not len(price1)==0:
                dict1.update({"price":int(price1[0].text[1:].replace(",",""))})
            else:
                dict1.update({"price":""})
            '''if not len(rating1)==0:
                dict1.update({"rating":rating1[0].text})'''
            dict1.update({"rating":""})
            dict1.update({"website":"Flipkart"})
            dict1.update({"url":newurl})
            dict1.update({"imgurl":img})  
            key="flip"+str(i)
            flipkart_dict.update({key:dict1})
              
        #print(review[0].text)
            #,"\t\t",rating[0].text,"\t\t")
        '''for a in color:
            print(a.text)
        for a in warranty:
            print(a.text)
        for a in extra:
            print(a.text)'''
    else :
        box1=soup.find_all('div',{"class":"_3liAhj _1R0K0g"}) 
        for item in box1:
            i=i+1
            dict1={}
            #image_url=item.find_all('img',{"class":"_3togXc"})[0]['src']
            #print(image_url)
            new=item.find_all('a',{"class":"_2cLu-l"})
            newurl="https://www.flipkart.com"+new[0]['href']
            #dict1.update({'link':newurl})
            name1=new[0]['title']#item.find_all("div",{"class":"_2mylT6"})
            price1=item.find_all("div",{"class":"_1vC4OE"})
            #review=soup1.find_all("span",{"class":"_38sUEc"})
            rating1=item.find_all("div",{"class":"hGSR34"})
            #warranty=soup1.find_all("div",{"class":"_3LXPtT"})
            #color=soup1.find_all("div",{"class":"_11cw91 _1-fCbU E753YP DgCx9f"})
            #extra=soup1.find_all("li",{"class":"_2-n-Lg col"})
            #warranty=soup1.find_all("div",{"class":"_3h7IGd"})
            if not len(name1)==0:
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
                dict1.update({"rating":""})
                
            dict1.update({"website":"Flipkart"})
            dict1.update({"url":newurl})
            dict1.update({"imgurl":img})    
            key="flip"+str(i)
            flipkart_dict.update({key:dict1})

    return flipkart_dict