"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('Hello Word')


# http://127.0.0.1:8000/bmi/?kg=65&heigh=179
def bmi(request):
    print(request.GET)
    heigh = float(request.GET.get('heigh'))
    kg = float(request.GET.get('kg'))
    bmi = kg / ((heigh / 100) ** 2)
    return render(request, 'bmi.html', {
        'bmi': bmi,
    })
    # return HttpResponse('BMI = {}'.format(bmi))


urlpatterns = [
    path('hello/', hello),
    path('bmi/', bmi),
    path('admin/', admin.site.urls),
]
