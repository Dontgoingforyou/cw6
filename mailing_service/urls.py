from django.urls import path

from .apps import MailingServiceConfig
from .views import MailingListView, MailingDeleteView, MailingUpdateView, MailingCreateView, MailingDetailView, \
    home_view

app_name = MailingServiceConfig.name

urlpatterns = [
    path('', home_view, name='home'),
    path('mailings', MailingListView.as_view(), name='mailing_list'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
]
