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
            print(new_search)
            result=obj.comp(new_search)
            return redirect('mainSearch')
    else:
        form=searching()  
    context={'form':form}
    return render(request,'price/index.html',context)
def mainSearch(request):
    context={"result":obj.result}
    for c in context['result']:
        print(c[1]['price'])
    return render(request,'price/search.html',context)
# Create your views here.
