from django.shortcuts import render,redirect
from .models import Client
from .forms import ClientForm

def client_list(request):
    clients = Client.objects.all()
    return render (request,"list.html",{"clients":clients})

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('где_вы_хотите_оказаться_после_сохранения')
    else:
        form = ClientForm()
    return render(request, 'your_app_name/client_form.html', {'form': form})