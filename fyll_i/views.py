from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'fyll_i/fyll_i.html')

def intervention(request):
    return render(request, 'fyll_i/intervention.html')

def uppna(request):
    return render(request, 'fyll_i/uppna.html')
