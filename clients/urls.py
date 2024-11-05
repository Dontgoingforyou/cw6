from django.urls import path
from django.views.decorators.cache import cache_page

from clients.apps import ClientsConfig
from clients.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = ClientsConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='clients_list'),
    path('<int:pk>/', cache_page(60)(ClientDetailView.as_view()), name='clients_detail'),
    path('create/', ClientCreateView.as_view(), name='clients_create'),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name='clients_update'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='clients_delete'),
]
