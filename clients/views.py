from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clients.models import Client


class ClientListView(ListView):
    model = Client
    context_object_name = 'clients'


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    context_object_name = 'client'


class ClientCreateView(CreateView):
    model = Client
    fields = ['email', 'full_name', 'comment', 'owner']
    success_url = reverse_lazy('clients:clients_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['email', 'full_name', 'comment', 'owner']
    success_url = reverse_lazy('clients:clients_list')


class ClientDeleteView(DeleteView):
    model = Client
    fields = ['email', 'full_name', 'comment', 'owner']
    success_url = reverse_lazy('clients:clients_list')
