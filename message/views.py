from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from message.models import Message


class MessageListView(ListView):
    model = Message
    context_object_name = 'messages'


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    context_object_name = 'message'


class MessageCreateView(CreateView):
    model = Message
    fields = ['topic', 'body', 'owner']
    success_url = reverse_lazy('message:message_list')

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