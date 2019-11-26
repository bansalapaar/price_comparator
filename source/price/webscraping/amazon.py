import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
def amazon_price(item_name):
	proxies = {'http': 'http://134.119.205.253:8080',
	'https': 'http://134.119.205.253:8080',}
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
	token1=re.split(',|;|:|_| |\.',item_name)
	print(token1)
	url='https://www.amazon.in/s?=aps&k='+"%20".join(token1)+"&ref=nb_sb_noss"
	r=requests.get(url,headers=headers)

	soup=BeautifulSoup(r.content,'html.parser')
	amazon_dict={}
	#print(soup)
	check=soup.find_all('div',{'class':'sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28'})
	i=0
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
			token2=re.split(',|;|:|_| |\.',(rn[0].text).lower())
			#print(token2)
			for a in token1:
				if not a in token2:
					flag=1
			if flag==1:
				continue
			dic1.update({"name":rn[0].text})
			dic1.update({"rating":((rr[0].text).split(' '))[0]})
			dic1.update({"price":int(rp[0].text.replace(",",""))})
			dic1.update({"website":"Amazon"})
			dic1.update({"url":'https://www.amazon.in'+rl[0]['href']})
			dic1.update({"imgurl":rm[0]['src']})  
			key="amazon"+str(i)
			amazon_dict.update({key:dic1})

	return amazon_dict
