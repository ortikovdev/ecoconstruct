from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mvphome.html', {'title': 'MVP | ECO CONSTRUCT'})


def emarket(request):
    return render(request, 'emarket/home.html', {'title': 'MVP | ECO CONSTRUCT'})

def trashremoving(request):
    return render(request, 'trash/home.html', {'title': 'MVP | ECO CONSTRUCT'})


def proclean(request):
    return render(request, 'clean/home.html', {'title': 'MVP | ECO CONSTRUCT'})

def aisolution(request):
    return render(request, 'ai/home.html', {'title': 'MVP | ECO CONSTRUCT'})