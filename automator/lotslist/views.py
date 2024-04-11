from django.shortcuts import render, redirect, HttpResponse, redirect,get_object_or_404
from django.http import HttpResponseNotFound, Http404, JsonResponse
from .forms import LotForm  # Убедитесь, что правильно импортировали LotForm
from .models import *

def add_lot(request,cl_inn):
    client = get_object_or_404(Client, cl_inn=cl_inn)
    if request.method == 'POST':
        form = LotForm(request.POST)
        if form.is_valid():
            # Сохраните лот с учетом клиента
            lot = form.save(commit=False)
            lot.client = client
            lot.save()
            return redirect("home")  # Убедитесь, что у вас есть URL с именем 'home' в urls.py
    else:
        form = LotForm()  # Используйте здесь LotForm вместо LotListBank
    
    return render(request, 'lotslist/add_lots.html', {'form': form})



def edit_lot(request, id):
    lot = get_object_or_404(LotListBank, id=id)
    if request.method == "POST":
        form = LotForm(request.POST, instance=lot)
        if form.is_valid():
            form.save()
            return redirect('lotlist') 
    else:
        form = LotForm(instance=lot)
    
    return render(request, 'lotslist/edit_lot.html', {'form': form})


def lot_list(request):
    lots = LotListBank.objects.all()
    context = {'lots':lots,}
    return render(request, "lotslist/lot_list.html", context=context)


