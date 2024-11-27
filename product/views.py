from django.shortcuts import render, redirect
from .models import PriceProd, Product

def saveprod(request):
    if request.METHOD == 'POST':
        nameprod_ = request.POST.get('nameprod')
        categoryprod_= request.POST.get('categoryprod')
        descprod_= request.POST.get('descprod')
        brandprod_ = request.POST.get('brandprod')
        manudateprod_ = request.POST.get('manudateprod')
        weightprod_ = float(request.POST.get('weightprod'))
        
        Product.objects.create(
            nameprod = nameprod_,
            categoryprod = categoryprod_,
            descprod = descprod_,
            brandprod = brandprod_,
            manudateprod = manudateprod_,
            weightprod = weightprod_
             
        )
        
        return render(request, "cadprod.html")
    return render(request, "cadprod.html")