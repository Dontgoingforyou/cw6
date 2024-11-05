from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clients.models import Client
from clients.services import get_clients_from_cache


class ClientListView(ListView):
    model = Client
    context_object_name = 'clients'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = get_clients_from_cache()
        return context


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    context_object_name = 'client'


class ClientCreateView(CreateView):
    model = Client
    fields = ['email', 'full_name', 'comment', 'owner']
    success_url = reverse_lazy('clients:clients_list')

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
