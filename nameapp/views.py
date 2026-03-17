from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import ContactDetail


class ContactDetailCreateView(LoginRequiredMixin, CreateView):
    model = ContactDetail
    fields = ['Name', 'Phone', 'address']
    template_name = 'nameapp/home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = ContactDetail.objects.all()
        return context


class ContactDetailUpdateView(LoginRequiredMixin, UpdateView):
    model = ContactDetail
    fields = ['Name', 'Phone', 'address']
    template_name = 'nameapp/update.html'
    success_url = '/'


class ContactDetailDeleteView(LoginRequiredMixin, DeleteView):
    model = ContactDetail
    success_url = '/'

