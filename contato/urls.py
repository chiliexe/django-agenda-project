from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.ContatoListView.as_view(), name='index'),
    path('create', views.ContatoCreateView.as_view(), name='create'),
    path('<int:pk>', views.ContatoDetailView.as_view(), name='detail')
]
