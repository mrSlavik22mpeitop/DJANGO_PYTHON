from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreate
from django.http import HttpResponse

#DataFlair
def index_product(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

def upload_product(request):
    upload = ProductCreate()
    if request.method == 'POST':
        upload = ProductCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index-product')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'products/upload_products.html', {'upload_products':upload,'title':"Добавить товар"})

def update_product(request, product_id):
    product_id = int(product_id)
    try:
        product_sel = Product.objects.get(id = product_id)
    except Product.DoesNotExist:
        return redirect('index-product')
    product_form = ProductCreate(request.POST or None, instance = product_sel)
    if product_form.is_valid():
       product_form.save()
       return redirect('index-product')
    return render(request, 'products/upload_products.html', {'upload_products':product_form, 'title':"Обновить товар"})

def delete_product(request, product_id):
    product_id = int(product_id)
    try:
        product_sel = Product.objects.get(id = product_id)
    except Product.DoesNotExist:
        return redirect('index-product')
    product_sel.delete()
    return redirect('index-product')