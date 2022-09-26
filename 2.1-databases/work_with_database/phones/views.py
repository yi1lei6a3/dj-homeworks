from django.shortcuts import render, redirect
from .models import Phone


SORTMAP = {
    'name': 'name',
    'min_price': 'price',
    'max_price': '-price',
}


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort:
        phones = Phone.objects.order_by(SORTMAP[sort])
    else:
        phones = Phone.objects.all()
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone, }
    return render(request, template, context)