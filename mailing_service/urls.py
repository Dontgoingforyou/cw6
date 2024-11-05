from django.urls import path
from django.views.decorators.cache import cache_page

from .apps import MailingServiceConfig
from .views import MailingListView, MailingDeleteView, MailingUpdateView, MailingCreateView, MailingDetailView, \
    home_view

app_name = MailingServiceConfig.name

urlpatterns = [
    path('', cache_page(60)(home_view), name='home'),
    path('mailings', MailingListView.as_view(), name='mailing_list'),
    path('mailings/<int:pk>/', cache_page(60)(MailingDetailView.as_view()), name='mailing_detail'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
]
