from django.shortcuts import render
from .models import Team
from products.models import Product

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_products = Product.objects.order_by('-created_date').filter(is_featured=True)
    all_products = Product.objects.order_by('-created_date')
    data = {
        'teams': teams,
        'featured_products': featured_products,
        'all_products': all_products,
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