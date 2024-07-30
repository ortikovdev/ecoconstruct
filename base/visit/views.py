from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main.html', {'title': 'ECO CONSTRUCT'})

def videorolik(request):
    return render(request, 'videorolik.html', {'title': 'ECO CONSTRUCT'})