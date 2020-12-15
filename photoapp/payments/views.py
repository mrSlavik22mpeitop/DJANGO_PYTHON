from django.db.models import F
from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentCreate
from django.http import HttpResponse

#DataFlair
def index_payment(request):
    print(Payment.objects.select_related('products_id').query)
    payments = Payment.objects.select_related('products_id').annotate(all_cost=F('products_id_id__price')*F('amount'))
    return render(request, 'payments/payments.html', {'payments': payments})

def upload_payment(request):
    upload = PaymentCreate()
    if request.method == 'POST':
        upload = PaymentCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index-payment')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'payments/upload_payments.html', {'upload_payments':upload,'title':"Добавить сотрудника"})

def update_payment(request, payment_id):
    payment_id = int(payment_id)
    try:
        payment_sel = Payment.objects.get(id = payment_id)
    except Payment.DoesNotExist:
        return redirect('index-payment')
    payment_form = PaymentCreate(request.POST or None, instance = payment_sel)
    if payment_form.is_valid():
       payment_form.save()
       return redirect('index-payment')
    return render(request, 'payments/upload_payments.html', {'upload_payments':payment_form, 'title':"Обновить сотрудника"})

def delete_payment(request, payment_id):
    payment_id = int(payment_id)
    try:
        payment_sel = Payment.objects.get(id = payment_id)
    except Payment.DoesNotExist:
        return redirect('index-payment')
    payment_sel.delete()
    return redirect('index-payment')