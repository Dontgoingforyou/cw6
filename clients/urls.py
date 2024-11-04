from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = ClientsConfig.name

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='clients_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='clients_detail'),
    path('clients/create/', ClientCreateView.as_view(), name='clients_create'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='clients_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='clients_delete'),
]
