from django.shortcuts import render, redirect, get_object_or_404
from .models import PriceProd, Product


def saveprod(request):
    if request.method == "POST":
        nameprod_ = request.POST.get("nameprod")
        categoryprod_ = request.POST.get("categoryprod")
        descprod_ = request.POST.get("descprod")
        brandprod_ = request.POST.get("brandprod")
        manudateprod_ = request.POST.get("manudateprod")
        weightprod_ = float(request.POST.get("weightprod"))

        Product.objects.create(
            nameprod=nameprod_,
            categoryprod=categoryprod_,
            descprod=descprod_,
            brandprod=brandprod_,
            manudateprod=manudateprod_,
            weightprod=weightprod_,
        )

        return render(request, "cadprod.html")
    return render(request, "cadprod.html")


def saveprice(request):
    if request.method == "POST":
        priceprod_ = float(request.POST.get("priceprod"))
        dateverify_ = request.POST.get("dateverify")
        codprod_ = Product(request.POST.get("product"))

        PriceProd.objects.create(
            priceprod=priceprod_, dateverify=dateverify_, codprod=codprod_
        )

        return redirect("saveprice")

    products = Product.objects.all()
    return render(request, "cadprice.html", {"products": products})


def historyprice(request, codprod):

    product_ = get_object_or_404(Product, pk=codprod)

    price_history_ = PriceProd.objects.filter(codprod=product_).order_by("-dateverify")

    return render(
        request,
        "pricehistory.html",
        {"product": product_, "price_history": price_history_},
    )
    
def productlist(request):
    
    products = Product.objects.all()
        
    return render(request, 'productlist.html', {'products': products})
