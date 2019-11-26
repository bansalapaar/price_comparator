"""
If the request method is POST then it will check whether the form is valid . If the form is valid it render price/search.html otherwise if the request is GET then it will render price/index.html.
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import searching
from price.webscraping import price_comparator
obj=price_comparator.price_comp()
def index(request):
    if request.method =='POST':
        form=searching(request.POST)
        if form.is_valid():
            new_search = request.POST['search']
            #print(new_search)
            result=obj.comp(new_search)
            return redirect('mainSearch')
    else:
        form=searching()  
    context={'form':form}
    return render(request,'price/index.html',context)
def mainSearch(request):
    context={"result":obj.result}
    return render(request,'price/search.html',context)
# Create your views here.
