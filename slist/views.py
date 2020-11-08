from django.shortcuts import render, redirect
from django.http import HttpResponse
from slist.models import Product, Supermarket
from slist.form import ProductForm, SupermarketForm
from django.contrib import messages
# Create your views here.


def slist(request):
    supermarkets = Supermarket.objects.all()
    query_products = Product.objects.filter()

    if request.POST:
        supermarket_id = request.POST.get('supermarket')
        query_products = Product.objects.filter(productbysupermarket__supermarket_id=supermarket_id)

    return render(request, 'list.html', {
        'supermarkets': supermarkets,
        'all_products': query_products
        }
    )


def home(request):
    if request.method == "POST":
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("Item added succesfully"))
        return redirect('home')
    else:
        all_products = Product.objects.all
        return render(request, 'home.html', {'all_products': all_products})


def delete(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('home')


def about(request):
    context = {
        'about_text': "Welcome to About Page"
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'contact_text': "Welcome to Contact Page"
    }
    return render(request, 'contact.html', context)
