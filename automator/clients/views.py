from django.shortcuts import render, redirect, HttpResponse, redirect,get_object_or_404
from django.http import HttpResponseNotFound, Http404, JsonResponse
import subprocess
from .models import *

menu = [
    {"title": "Войти", "url_name": "login"},
    {"title": "Главная", "url_name": "home"},
    {"title": "Список клиентов", "url_name": "clients_list"},
    {"title": "Добавить клиента", "url_name": "add_client"},
    # {"title": "найти клиента", "url_name": "client"},
    {"title": "Контакты", "url_name": "contact"},
    {"title": "О нас", "url_name": "about"},
]

def run_script():
    python_exec_path = "/Users/nikolay/Documents/made_doc_for_ol/.venv/bin/python3"
    # script_path =  '/Users/nikolay/Documents/made_doc_for_ol/doc_made.py'
    script_path = "/Users/nikolay/Documents/BiddingAuto/temp.py"
    result = subprocess.run([python_exec_path, script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

def run_script_view(request):
    stdout, stderr = run_script()
    return JsonResponse({'stdout': stdout, 'stderr': stderr})

def index(request):
    return render(
        request, "clients/index.html", {"menu": menu, "title": "главная страница"}
    )


def about(request):
    return render(request, "clients/about.html", {"menu": menu, "title": "о сайте"})


def clients_list(request):
    clients = Client.objects.all()
    context = {'clients':clients,"menu":menu,'title':"главная страница"}
    return render(request, "clients/client_list.html", context=context)



def show_client(request,cl_inn):
    client = get_object_or_404(Client,cl_inn="561211426761")
    return render(request, "clients/show_client.html", {"client": client})

def add_client(request):
    return HttpResponse("добавить клиента")

def contact(request):
    return HttpResponse("контакты")

def login(request):
   return HttpResponse("авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
