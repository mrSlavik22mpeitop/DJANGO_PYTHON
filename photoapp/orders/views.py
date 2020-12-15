from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderCreate
from django.http import HttpResponse

#DataFlair
def index_order(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders.html', {'orders': orders})

def upload_order(request):
    upload = OrderCreate()
    if request.method == 'POST':
        upload = OrderCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index-order')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'orders/upload_orders.html', {'upload_orders':upload,'title':"Добавить покупку"})

def update_order(request, order_id):
    order_id = int(order_id)
    try:
        order_sel = Order.objects.get(id = order_id)
    except Order.DoesNotExist:
        return redirect('index-order')
    order_form = OrderCreate(request.POST or None, instance = order_sel)
    if order_form.is_valid():
       order_form.save()
       return redirect('index-order')
    return render(request, 'orders/upload_orders.html', {'upload_orders':order_form, 'title':"Обновить покупку"})

def delete_order(request, order_id):
    order_id = int(order_id)
    try:
        product_sel = Order.objects.get(id = order_id)
    except Order.DoesNotExist:
        return redirect('index-order')
    order_sel.delete()
    return redirect('index-order')