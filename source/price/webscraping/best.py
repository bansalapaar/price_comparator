import requests
from bs4 import BeautifulSoup
import pandas as pd
def paytmbest(url):
    dict1={}
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup)
    img=soup.find('img',attrs={"class":"_3v_O"})
    dict1.update({'img':img['src']})
    name=soup.find('h1',attrs={"class":"NZJI"})
    print(name.text)
    dict1.update({'name':name.text})
    rating=soup.find('div',attrs={"class":"_2dWu"})
    print(rating.text)
    dict1.update({'rating':rating.text})
    reviews=soup.find('div',attrs={"class":'_38Tb'})
    print(reviews.text)
    dict1.update({'reviews':reviews.text})
    price=soup.find('span',attrs={'class':'_1V3w'})
    print(price.text)
    offer=soup.find('div',attrs={'class':'A9RM'})
    print(offer.text)
    returnpolicy=soup.find('div',attrs={'class':'_15EQ'})
    print(returnpolicy)




