from django.shortcuts import render


def index(request):
    return render(request, 'GAK6/index.html')


def calculate(request):
    result = None
    square_side = None
    if request.method == 'POST':
        try:
            if 'reset' in request.POST:
                square_side = ''
                square_volume = None
            else:
                square_side = int(request.POST.get('square_side', ''))
                result = square_side ** 3
        except (TypeError, ValueError):
            result = 'Input Error'
    return render(request, 'GAK6/calculate.html', {'result': result, 'square_side': square_side})
