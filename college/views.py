from django.shortcuts import render

def index(request):
    template = 'index.html'
    data = {}
    return render(request, template, data)