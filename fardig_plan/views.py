from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'fardig_plan/fardig_plan.html')