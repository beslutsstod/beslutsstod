from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name='baseutils'),
    path('update_server/', views.update, name='update')
]
