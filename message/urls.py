from django.urls import path
from django.views.decorators.cache import cache_page

from message.apps import MessageConfig
from message.views import MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView

app_name = MessageConfig.name

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path('<int:pk>/', cache_page(60)(MessageDetailView.as_view()), name='message_detail'),
    path('create/', MessageCreateView.as_view(), name='message_create'),
    path('<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
]
