from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
import razorpay
from django.views.decorators.csrf import csrf_exempt
from .models import Forms
from .forms import modelForm
from django.conf import settings

def index(request):
    context = {}
    form = modelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form

    if request.method == 'POST':
        #name = request.POST['name']
        amt = float(request.POST['amount'])
        amount = amt * 100
        client = razorpay.Client(auth = (settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET_KEY))

        client.set_app_details({"title" : "Django", "version" : "3.2.5"})

        payment = client.order.create({'amount' : amount, 
                                        'currency' : 'INR',
                                        'payment_capture' : '1'})
        
        data = {
                'payment' : payment
                }

        return render(request, 'redirect.html', data)
    return render(request, 'index.html', context)

@csrf_exempt
def success(request):
    return render(request, 'success.html')