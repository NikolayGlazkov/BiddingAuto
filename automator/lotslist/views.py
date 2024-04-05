from django.shortcuts import render, redirect, HttpResponse, redirect,get_object_or_404
from django.http import HttpResponseNotFound, Http404, JsonResponse

from .models import *

# Create your views here.
def add_lot(request):
    return HttpResponse("добавить лот")
