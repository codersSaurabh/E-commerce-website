from django.shortcuts import render
from django.http import HttpResponse 
from.models import Product,Contact,orders,orderUpdate
from math import ceil
import json
# Create your views here.

def index(request):
   
    allprod=[]
    catprod=Product.objects.values('category','id')
    cats={item['category']for item in catprod}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslide=n//4+ceil((n/4-(n//4)))
        allprod.append([prod,range(1,nslide),nslide])
    params={'allProds':allprod}
    return render(request,'shop/index.html',params)
def tracker(request):

    if(request.method=="POST"):
        orderid= request.POST.get("orderid","")
        email= request.POST.get("email","")
        try:
            order=orders.objects.filter(order_id=orderid,email=email)
            if(len(order)>0):
                update=orderUpdate.objects.filter(order_id=orderid)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.itemstamp})
                    response=json.dumps([updates,order[0].item_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
           
    return render(request,'shop/tracker.html')
def about(request):
    return render(request,'shop/about.html')
def search(request):
    
    if(request.method=="POST"):
        name= request.POST.get("search","")
        name=name.lower().capitalize()
        allprod=[]
        catprod=Product.objects.values('category','id')
        cats={item['category']for item in catprod}
        if(name==""):
            
            for cat in cats:
                prod=Product.objects.filter(category=cat)
                n=len(prod)
                nslide=n//4+ceil((n/4-(n//4)))
                allprod.append([prod,range(1,nslide),nslide])
            params={'allProds':allprod}
        else:
            prod=Product.objects.filter(category=name)
            n=len(prod)
            nslide=n//4+ceil((n/4-(n//4)))
            allprod.append([prod,range(1,nslide),nslide])
            params={'allProds':allprod,}
        if(len(prod)):
            return render(request,'shop/search.html',params)
        else:
            return HttpResponse("<center style='margin-top:50px'><h2>No Result Found</h2><h4>Click here to go Shop<button><a href='/'>Click Here</a></button></h4>")
        return render(request,'shop/search.html')
def productview(request,prid):
    #fetch the product using the id
    product=Product.objects.filter(id=prid)
    print(product[0].id)
    return render(request,'shop/prodview.html',{'product':product[0]})
def checkout(request):
    if(request.method=="POST"):
        json=request.POST.get('itemsjson','')
        name= request.POST.get("name","")
        email= request.POST.get("email","")
        address= request.POST.get("address1","")+" "+request.POST.get('address2',"")
        city= request.POST.get("city","")
        state= request.POST.get("state","")
        zip_code=request.POST.get("zip_code","")
        phone=request.POST.get("phone","")
        if(name!="" and email!=""and address!=""and city!=""and json!=""and state!=""and phone!=""and zip_code!=""):
            order=orders(item_json=json,name=name,email=email ,address=address,state=state,city=city,zip_code=zip_code,phone=phone)
            order.save()
            thank=True
            update=orderUpdate(order_id=order.order_id,update_desc="The Order has been places")
            id=order.order_id
            update.save()
            return render(request,'shop/checkout.html',{'thank':thank,'id':id})
        else:
            return render(request,'shop/checkout.html',{'error':True})
    return render(request,'shop/checkout.html')
        
    
def contact(request):
    if(request.method=="POST"):

        name= request.POST.get("name","")
        email= request.POST.get("email","")
        phone=request.POST.get("phone","")
        desc=request.POST.get("desc","")
        if(name!="" and email!="" and desc!="" and phone!=""):
            contact=Contact(customer_name=name,customer_email=email,customer_phone=phone,customer_query=desc)
            contact.save()
            return render(request,'shop/contact.html',{'success':True})

        else:
            return render(request,'shop/contact.html',{'error':True})

    return render(request,'shop/contact.html')
