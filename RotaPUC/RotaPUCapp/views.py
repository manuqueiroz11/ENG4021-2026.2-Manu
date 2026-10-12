from django.shortcuts import render

# Create your views here.
def paises(request):
    return render(request, "paises.html")