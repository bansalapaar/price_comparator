"""
amazon.py
================
This module is used to do webscraping on amazon website. It searches the product on the amazon website entered by user and store the important information related to product
"""

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

def amazon_price(item_name):
	"""
	This function store the important information related to the searched product
	Parameters
	-----------------
	item_name is the name of the product entered by the user to be searched
	"""

	proxies = {'http': 'http://134.119.205.253:8080',
	'https': 'http://134.119.205.253:8080',}
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
	token1=re.split(',|;|:|_| |\.',item_name)
	#print(token1)
	url='https://www.amazon.in/s?=aps&k='+"%20".join(token1)+"&ref=nb_sb_noss"
	r=requests.get(url,headers=headers)
	soup=BeautifulSoup(r.content,'html5lib')
	amazon_dict={}
	check=soup.find_all('li',{'class':'a-carousel-card'})
	#print(check)
	i=0
	if not check==None:
		"""
		This for loop iterates each item related to product on the amazon webpage and store information about it 
		"""
		for item in check:
			#print(item)
			dic1={}
			rn= item.find('span',attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
			rm=item.find('img',attrs={"class":"s-image"})
			link=item.find('a',attrs={'class':'a-size-base'})
			rp= item.find('span',attrs={'class':'a-price-whole'})
			rr= item.find('span',attrs={'class':'a-icon-alt'})
			#print(rn.text,rm['src'],rp.text,rr.text,link['href'])
			flag=0
			i=i+1
			if i>=6:
				break
			dic1.update({"name":rn.text})
			dic1.update({"rating":((rr.text).split(' '))[0]})
			dic1.update({"price":int(rp.text.replace(",",""))})
			dic1.update({"website":"Amazon"})
			if link==None:
				continue
			dic1.update({"url":'https://www.amazon.in'+link['href']})
			dic1.update({"imgurl":rm['src']})  
			key="amazon"+str(i)
			#print(dic1)
			amazon_dict.update({key:dic1})
	else:
		check=soup.find_all('div',{'class':'sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28'})
		i=0
		"""
		for loop to extract item information when when page item shows horizontally
		"""
		for item in check:
			#print(i)
			dic1={}
			rl=item.find_all('a',attrs={"class":"a-link-normal"})
			rm=item.find_all('img',attrs={"class":"s-image"})
			rp= item.find_all('span',attrs={'class':'a-price-whole'})
			rr= item.find_all('span',attrs={'class':'a-icon-alt'})
			rn= item.find_all('span',attrs={'class':'a-size-medium a-color-base a-text-normal'})
			if not(len(rp)==0) and not(len(rr)==0) and not(len(rn)==0) and not(len(rm)==0) and not(len(rl)==0):
				flag=0
				i=i+1
				if i>=6:
					break
				dic1.update({"name":rn[0].text})
				dic1.update({"rating":((rr[0].text).split(' '))[0]})
				dic1.update({"price":int(rp[0].text.replace(",",""))})
				dic1.update({"website":"Amazon"})
				dic1.update({"url":'https://www.amazon.in'+rl[0]['href']})
				dic1.update({"imgurl":rm[0]['src']})  
				key="amazon"+str(i)
				amazon_dict.update({key:dic1})

	return amazon_dict

