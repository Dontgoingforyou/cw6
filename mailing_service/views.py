from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blogs.models import BlogPost
from mailing_service.models import Mailing, Client


def home_view(request):
    total_mailings = Mailing.objects.count()
    active_mailings = Mailing.objects.filter(is_active=True).count()
    unique_clients = Client.objects.values('email').distinct().count()
    random_articles = BlogPost.objects.order_by('?')[:3]

    context = {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'unique_clients': unique_clients,
        'random_articles': random_articles,
    }
    return render(request, 'mailing_service/home.html', context)

class MailingListView(ListView):
    model = Mailing
    context_object_name = 'mailings'


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    context_object_name = 'mailing'


class MailingCreateView(CreateView):
    model = Mailing
    fields = ['start_datetime', 'periodicity', 'message', 'clients', 'owner']
    success_url = reverse_lazy('mailing_service:mailing_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    fields = ['start_datetime', 'periodicity', 'message', 'clients', 'owner']
    success_url = reverse_lazy('mailing_service:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    fields = ['start_datetime', 'periodicity', 'message', 'clients', 'owner']
    success_url = reverse_lazy('mailing_service:mailing_list')
