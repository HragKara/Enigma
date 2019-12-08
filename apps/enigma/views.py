# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):

    return render(request, 'enigma/index.html')

def pricing(request):

    return render(request, 'enigma/pricing.html')

def platinum(request):

    return render(request, 'enigma/buy.html')