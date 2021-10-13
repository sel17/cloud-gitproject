from django.shortcuts import render
from .models import Team
from products.models import Product

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_products = Product.objects.order_by('-created_date').filter(is_featured=True)
    all_products = Product.objects.order_by('-created_date')
    #search_fields = Product.objects.values('model', 'city', 'year', 'body_style')
    model_search = Product.objects.values_list('model', flat=True).distinct()
    city_search = Product.objects.values_list('city', flat=True).distinct()
    year_search = Product.objects.values_list('year', flat=True).distinct()
    body_style_search = Product.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_products': featured_products,
        'all_products': all_products,
        #'search_fields': search_fields,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')