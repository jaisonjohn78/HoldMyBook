from django.http import HttpResponse
from django.shortcuts import render


def aboutUs(request):
    return HttpResponse("This is the about us page")

def Home(request):
    return render(request, "index.html")