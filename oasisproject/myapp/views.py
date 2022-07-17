from django.shortcuts import get_object_or_404, render
from .models import yeosuRestaurant, jeonjuRestaurant, product, wandoRestaurant

client_id = "lxJGkOeMAIMOo6Tf5dZx"
client_secret = "Y79oJ07GkN"
# Create your views here.
def home(request):
    return render(request, 'index.html')

def map(request):
    return render(request, 'mapindex.html')

def searchshow(request):
    return render(request, 'map1.html')
    
def yeosu(request):
    restaurants = yeosuRestaurant.objects.all
    return render(request, 'yeosu.html', {'restaurants':restaurants})

def jeonju(request):
    restaurants = jeonjuRestaurant.objects.all
    return render(request, 'jeonju.html', {'restaurants':restaurants})

def wando(request):
    restaurants = wandoRestaurant.objects.all
    return render(request, 'wando.html', {'restaurants':restaurants})

def productshow(request):
    restaurants = jeonjuRestaurant.objects.all
    return render(request, 'product.html', {'restaurants':restaurants})

def detail(request, product_id):
    product_detail = get_object_or_404(product, pk=product_id)
    return render(request, 'prdetail.html', {'product':product_detail})

def mypage(request):
    return render(request, 'mypage.html')