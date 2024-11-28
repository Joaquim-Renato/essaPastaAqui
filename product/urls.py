from django.urls import path
from . import views

urlpatterns = [
    path('saveprod/', views.saveprod, name='saveprod'),
    path('saveprice/', views.saveprice, name='saveprice'),
    path('historyprice/', views.historyprice, name='historyprice')
]