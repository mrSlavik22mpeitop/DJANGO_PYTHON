from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerCreate
from django.http import HttpResponse

#DataFlair
def index_customer(request):
    customers = Customer.objects.all()
    return render(request, 'customers/photoapp.html', {'customers': customers})

def upload_customer(request):
    upload = CustomerCreate()
    if request.method == 'POST':
        upload = CustomerCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index-customer')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'customers/upload_form.html', {'upload_form':upload,'title':"Добавить покупателя"})

def update_customer(request, customer_id):
    customer_id = int(customer_id)
    try:
        customer_sel = Customer.objects.get(id = customer_id)
    except Customer.DoesNotExist:
        return redirect('index-customer')
    customer_form = CustomerCreate(request.POST or None, instance = customer_sel)
    if customer_form.is_valid():
       customer_form.save()
       return redirect('index-customer')
    return render(request, 'customers/upload_form.html', {'upload_form':customer_form, 'title':"Обновить покупателя"})

def delete_customer(request, customer_id):
    customer_id = int(customer_id)
    try:
        customer_sel = Customer.objects.get(id = customer_id)
    except Customer.DoesNotExist:
        return redirect('index-customer')
    customer_sel.delete()
    return redirect('index-customer')