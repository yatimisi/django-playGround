from django.http import HttpResponse
from django.shortcuts import render

from .forms import BmiForm

def hello(request):
    return HttpResponse('Hello Word')


# http://127.0.0.1:8000/bmi/?kg=65&heigh=179
def bmi(request):
    if request.method == 'POST':
        heigh = request.POST.get('heigh', '')
        kg = request.POST.get('kg', '')
        if heigh == '' or kg == '':
            return HttpResponse("heigh or kg is None")
        heigh = float(heigh)
        kg = float(kg)
        bmi = kg / ((heigh / 100) ** 2)
        return render(request, 'bmi.html', {
            'bmi': bmi, 
        })

    form = BmiForm()
    return render(request, 'bmi-input.html',{
        'form': form
    })