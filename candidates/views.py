from django.shortcuts import render, redirect

from .models import Candidate
from .forms import CandidateForm

def index(request):
    candidates = Candidate.objects.all()
    return render(request, 'Candidate_list.html', {
        'candidates': candidates,
    })


def add(request):
    form = CandidateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/candidates/')

    return render(request, 'Candidate_add.html', {
        'form': form,
    })