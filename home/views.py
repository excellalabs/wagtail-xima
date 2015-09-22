__author__ = 'Nick'

from django.shortcuts import render, redirect, get_object_or_404, render_to_response

from home.models import *
from home.forms import *

# def description_parser(description):
#     if "<img>"

def product_list(request):
    return render(request, 'product_list.html', {'product_list': InventoryItem.objects.all()})

def inventory_logs(request):
    return render(request, 'inventory_logs.html', {'product_list': InventoryItem.objects.all()})

def order(request, product_id):
    if request.POST:
        form = FormOrder(request.POST)
        if form.is_valid():
            product = InventoryItem.objects.get(id=product_id)
            order_quantity = form.cleaned_data['quantity']
            product.stocked_quantity += order_quantity
            product.save()
            return redirect("/inventory_logs")
    else:
        product = InventoryItem.objects.get(id=product_id)
        form = FormOrder()
        return render(request, 'order.html', {'product': product, 'form': form})
