from django.http import HttpResponse
from django.shortcuts import render

from .forms import BmiForm

def hello(request):
    return HttpResponse('Hello Word')


# http://127.0.0.1:8000/bmi/?kg=65&heigh=179
def bmi(request):
    form = BmiForm(request.POST or None)
    if form.is_valid():
        heigh = form.cleaned_data['heigh']
        kg = form.cleaned_data['kg']
        bmi = w / ((h / 100) ** 2)
        return render(request, 'bmi.html', {'bmi': bmi})

    return render(request, 'bmi-input.html', {'form': form})

