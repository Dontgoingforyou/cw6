from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blogs.models import BlogPost
from mailing_service.models import Mailing, Client
from mailing_service.services import get_mailings_from_cache


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailings'] = get_mailings_from_cache()
        return context


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    context_object_name = 'mailing'


class MailingCreateView(CreateView):
    model = Mailing
    fields = ['start_datetime', 'periodicity', 'message', 'clients']
    success_url = reverse_lazy('mailing_service:mailing_list')

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    fields = ['start_datetime', 'periodicity', 'message', 'clients']
    success_url = reverse_lazy('mailing_service:mailing_list')
    permission_required = (
        'mailing_service.can_view_mailing', 'mailing_service.can_block_user', 'mailing_service.can_disable_mailing')

    def get_object(self, queryset=None):
        mailing = get_object_or_404(Mailing, id=self.kwargs['pk'])
        if mailing.owner != self.request.user:
            raise PermissionDenied("У вас нет прав редактировать эту рассылку.")
        return mailing


class MailingDeleteView(DeleteView):
    model = Mailing
    fields = ['start_datetime', 'periodicity', 'message', 'clients']
    success_url = reverse_lazy('mailing_service:mailing_list')
