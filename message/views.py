from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from message.models import Message
from message.services import get_messages_from_cache


class MessageListView(ListView):
    model = Message
    context_object_name = 'messages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = get_messages_from_cache()
        return context


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    context_object_name = 'message'


class MessageCreateView(CreateView):
    model = Message
    fields = ['topic', 'body', 'owner']
    success_url = reverse_lazy('message:message_list')

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ['topic', 'body', 'owner']
    success_url = reverse_lazy('message:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    fields = ['topic', 'body', 'owner']
    success_url = reverse_lazy('message:message_list')
