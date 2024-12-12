from django.shortcuts import render, redirect, get_object_or_404
from .models import PriceProd, Product
from .forms import PriceProdForm


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

def pricechart(request, codprod):
    
    product_ = get_object_or_404(Product, pk=codprod)
    
    price_history_ = PriceProd.objects.filter(codprod=product_).order_by("-dateverify")
    
    dates_ = [entry.dateverify.strftime('%d-%m-%Y')
              for entry in price_history_]
    prices_ = [float(entry.priceprod)
              for entry in price_history_]
    
    return render(request, 'pricechart.html', {'product': product_,
                                               'chartdata' : {
                                                   'dates' : dates_,
                                                   'prices': prices_
                                                }})
    
def index(request):
    return render(request, 'index.html')  

def deleteprice(request, codprice):
    
    history_ = PriceProd.objects.get(codprice=codprice)
    prod_ = history_.codprod
    
    history_.delete()
    return redirect('historyprice', prod_.codprod)

def editprice(request, codprice):
    price_ = get_object_or_404(PriceProd, pk=codprice)
    
    if request.method == "POST":
        form = PriceProdForm(request.POST, instance=price_)
        if form.is_valid():
            form.save()  # Salva a alteração no banco de dados
            return redirect('historyprice', codprod=price_.codprod.codprod)  # Redireciona para a página de histórico de preços
    else:
        form = PriceProdForm(instance=price_)
    
    return render(request, 'editprice.html', {'form': form, 'price': price_})




def deleteprod(request, codprod):
    
    products_ = Product.objects.get(codprod=codprod)
    pd_ = products_.codprod
    
    products_.delete()
    return redirect('productlist.html',pd_.codprod)
