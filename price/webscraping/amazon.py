import requests
from bs4 import BeautifulSoup
import pandas as pd
def amazon_price(item_name):

	url='https://www.amazon.in/s?k='+item_name+'&ref=nb_sb_noss_2'
	user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
	headers = {'User-Agent': user_agent}
	r=requests.get(url,headers=headers)

	soup=BeautifulSoup(r.content,'html.parser')
	amazon_dict={}

	check=soup.find_all('div',{'class':'sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28'})
	i=0
	for item in check:
		i=i+1
		dic1={}
		rl=item.find_all('a',attrs={"class":"a-link-normal"})
		rm=item.find_all('img',attrs={"class":"s-image"})
		rp= item.find_all('span',attrs={'class':'a-price-whole'})
		rr= item.find_all('span',attrs={'class':'a-icon-alt'})
		rn= item.find_all('span',attrs={'class':'a-size-medium a-color-base a-text-normal'})
		if not(len(rp)==0) and not(len(rr)==0) and not(len(rn)==0) and not(len(rm)==0) and not(len(rl)==0):
			dic1.update({"name":rn[0].text})
			dic1.update({"rating":((rr[0].text).split(' '))[0]})
			dic1.update({"price":int(rp[0].text.replace(",",""))})
			dic1.update({"website":"Amazon"})
			dic1.update({"url":'https://www.amazon.in'+rl[0]['href']})
			dic1.update({"imgurl":rm[0]['src']})  
			key="amazon"+str(i)
			amazon_dict.update({key:dic1})

	return amazon_dict

