from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'fyll_i/fyll_i.html')