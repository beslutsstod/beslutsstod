from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name='fyll-i'),
    path('/intervention', views.intervention, name='fyll-i/intervention'),
    path('/uppna', views.uppna, name='fyll-i/uppna'),
    path('/sammanhang', views.sammanhang, name='fyll-i/sammanhang'),
]
