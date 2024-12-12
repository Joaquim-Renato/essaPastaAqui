from django.urls import path
from . import views

# <int:codprod> é como um "filtro" / recorte de determinado parâmetro 
urlpatterns = [
    path('saveprod/', views.saveprod, name='saveprod'),
    path('saveprice/', views.saveprice, name='saveprice'),
    path('historyprice/<int:codprod>', views.historyprice, name='historyprice'),
    path('productlist/', views.productlist, name='productlist' ),
    path('pricechart/<int:codprod>', views.pricechart, name='pricechart'),
    path('', views.index, name='index'),
    path('deleteprice/<int:codprice>/', views.deleteprice, name='deleteprice'),
    path('editprice/<int:codprice>', views.editprice, name='editprice'),
    path('deleteprod/<int:codprod>/', views.deleteprod, name='deleteprod'),
    path('editproduct/<int:codprod>/', views.editproduct, name='editproduct')
]