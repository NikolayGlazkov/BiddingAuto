from django.shortcuts import render, redirect, HttpResponse, redirect,get_object_or_404
from django.http import HttpResponseNotFound, Http404, JsonResponse
import subprocess
from .models import *
from .forms import ClientForm
from lotslist.views import *
from lotslist.models import *


def run_script():
    python_exec_path = "/Users/nikolay/Documents/made_doc_for_ol/.venv/bin/python3"
    # script_path =  '/Users/nikolay/Documents/made_doc_for_ol/doc_made.py'
    script_path = "/Users/nikolay/Documents/made_doc_for_ol/doc_made.py"
    result = subprocess.run([python_exec_path, script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

def run_script_view(request):
    stdout, stderr = run_script()
    return JsonResponse({'stdout': stdout, 'stderr': stderr})

def index(request):
     return render(request,"clients/index.html")

def contact(request):
    return HttpResponse("контакты")

def login(request):
   return HttpResponse("авторизация")

def about(request):
    return render(request, "clients/about.html", {"title": "о сайте"})


def clients_list(request):
    clients = Client.objects.all()
    context = {'clients':clients,'title':"главная страница"}
    return render(request, "clients/client_list.html", context=context)

def edit_client(request, cl_inn):
    user = get_object_or_404(Client, cl_inn = cl_inn)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('clients_list')  # Предположим, у вас есть URL с именем 'users_list', который ведёт к списку пользователей
    else:
        form = ClientForm(instance=user)
    
    return render(request, '/Users/nikolay/Documents/BiddingAuto/automator/templates/clients/edit_client.html', {'form': form})

def find_client(request):
    if request.method == 'GET':
        query = request.GET.get('query')  # Получаем значение запроса поиска
        if query:
            query = query.capitalize()
            # Выполняем поиск клиента по ИНН или фамилии
            clients = Client.objects.filter(cl_inn=query) | Client.objects.filter(surname=query)
            return render(request, 'clients/client_list.html', {'clients': clients, 'title': 'Результаты поиска'})
    # Если запрос не был выполнен или не был найден клиент, возвращаем пустую страницу
    return render(request, 'clients/client_list.html', {'clients': [], 'title': 'Результаты поиска'})

def show_client(request, cl_inn):
    client = get_object_or_404(Client, cl_inn=cl_inn)
    # Получение всех лотов, принадлежащих этому клиенту
    lots = LotListBank.objects.filter(client=client)
    
    return render(request, 'clients/show_client.html', {'client': client, 'lots': lots})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clients_list")  # Замените 'success_url' на адрес, куда вы хотите перенаправить пользователя после успешного заполнения формы
    else:
        form = ClientForm()
    
    return render(request, 'clients/add_client.html', {'form': form})

def delete_client(request,cl_inn):
    client = get_object_or_404(Client,cl_inn=cl_inn)
    client.delete()
    return redirect("clients_list")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
