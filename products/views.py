from django.shortcuts import get_object_or_404, render

from .models import Product

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def products (request):
    products = Product.objects.order_by('-created_date')
    paginator = Paginator(products, 4) #howmanyproductsperpage
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)



    model_search = Product.objects.values_list('model', flat =True).distinct()
    city_search = Product.objects.values_list('city', flat =True).distinct()
    year_search = Product.objects.values_list('year', flat =True).distinct()
    body_style_search = Product.objects.values_list('body_style', flat =True).distinct()
    


    data = {
        'products': paged_products,
         #'search_fields': search_fields,
         'model_search':model_search,
         'city_search':city_search,
         'year_search':year_search,
        'body_style_search':body_style_search,

    }
    return render (request, 'products/products.html', data)


def product_detail (request, id):
    single_product = get_object_or_404(Product, pk =id)

    data = {
        'single_product' : single_product,
    }

    return render (request, 'products/product_detail.html', data)

def search(request):
    products = Product.objects.order_by('-created_date')

    model_search = Product.objects.values_list('model', flat =True).distinct()
    city_search = Product.objects.values_list('city', flat =True).distinct()
    year_search = Product.objects.values_list('year', flat =True).distinct()
    body_style_search = Product.objects.values_list('body_style', flat =True).distinct()
    


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = products.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            products = products.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            products = products.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            products = products.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            products = products.filter(body_style__iexact=body_style)

    
    if 'min-price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if max_price:
            products = products.filter(price_gte = min_price, price_lte = max_price) #gte means greater than equal to 



    data = {
        'products': products,
         #'search_fields': search_fields,
         'model_search':model_search,
         'city_search':city_search,
         'year_search':year_search,
        'body_style_search':body_style_search,

    }
    return render(request, 'products/search.html', data)