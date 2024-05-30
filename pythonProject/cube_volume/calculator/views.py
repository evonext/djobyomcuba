# calculator/views.py
from django.shortcuts import render
from django.http import HttpResponseBadRequest

def index(request):
    return render(request, 'calculator/index.html', {'side': None, 'volume': None})

def calculate(request):
    if request.method == 'POST':
        try:
            side = float(request.POST.get('side'))
            volume = side ** 3
            return render(request, 'calculator/index.html', {'side': side, 'volume': volume})
        except ValueError:
            return HttpResponseBadRequest("Invalid input. Please enter a valid number.")
    return HttpResponseBadRequest("Invalid request method.")
