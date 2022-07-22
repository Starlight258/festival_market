from django.shortcuts import get_object_or_404, render
from .models import yeosuRestaurant, jeonjuRestaurant, product, wandoRestaurant, wandoVisit, yeosuVisit
from .models import jeonjuVisit, gwangyangVisit, goheungVisit, goheungRestaurant, gwangyangRestaurant
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
    visit = yeosuVisit.objects.all
    return render(request, 'yeosu.html', {'restaurants':restaurants,'visit':visit})

def jeonju(request):
    restaurants = jeonjuRestaurant.objects.all
    visit = jeonjuVisit.objects.all
    return render(request, 'jeonju.html', {'restaurants':restaurants,'visit':visit})

def wando(request):
    restaurants = wandoRestaurant.objects.all
    visit = wandoVisit.objects.all
    return render(request, 'wando.html', {'restaurants':restaurants,'visit':visit})

def productshow(request):
    restaurants = jeonjuRestaurant.objects.all
    return render(request, 'product.html', {'restaurants':restaurants})

def detail(request, product_id):
    product_detail = get_object_or_404(product, pk=product_id)
    return render(request, 'prdetail.html', {'product':product_detail})

def mypage(request):
    return render(request, 'sidebar.html')
def mypage2(request):
    return render(request, 'sidebar.html')

def tempindex(request):
    return render(request, 'tempindex.html')

def gwangyang(request):
    restaurants = gwangyangRestaurant.objects.all
    visit = gwangyangVisit.objects.all
    return render(request, 'gwangyang.html', {'restaurants':restaurants, 'visit':visit})

def goheung(request):
    restaurants = goheungRestaurant.objects.all
    visit = goheungVisit.objects.all
    return render(request, 'goheung.html', {'restaurants':restaurants, 'visit':visit})

def course(request):
    return render(request, 'course.html')

def home2(request):
    return render(request, 'index2.html')

def festival(request):
    restaurants = jeonjuRestaurant.objects.all
    visit = jeonjuVisit.objects.all
    return render(request, 'festivaldetail.html', {'restaurants':restaurants, 'visit':visit})