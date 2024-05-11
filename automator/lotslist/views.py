from django.shortcuts import render, redirect, HttpResponse, redirect,get_object_or_404
from django.http import HttpResponseNotFound, Http404, JsonResponse
from .forms import LotForm  # Убедитесь, что правильно импортировали LotForm
from .models import *
from django.http import JsonResponse
from .models import LotListBank
from .serializers import LotSerializer
from rest_framework import generics

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


# def fetch_lot_efrsb_urls():
#     lots = LotListBank.objects.all()
#     urls = [lot.lot_efrsb_urls for lot in lots]
#     return urls

class LotListAPIView(generics.ListAPIView):
    queryset = LotListBank.objects.all()
    serializer_class = LotSerializer

# не работает:
def lot_events(request):
    lots = LotListBank.objects.all()
    lot_data = [
        {
            'title': f'Лоhт {lot.id}',
            'start': lot.auction_day.strftime('%Y-%m-%d'), # или lot.end_of_feed, в зависимости от того, какую дату вы хотите использовать
            'url': f'/path/to/lot/{lot.id}/'  # Ссылка для просмотра деталей лота
        } for lot in lots
    ]
    return JsonResponse(lot_data, safe=False)
