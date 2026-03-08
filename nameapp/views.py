from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView
from .models import ContactDetail


class ContactDetailCreateView(CreateView):
    model = ContactDetail
    fields = ['Name', 'Phone', 'address']
    template_name = 'nameapp/home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = ContactDetail.objects.all()
        return context


class ContactDetailDeleteView(DeleteView):
    model = ContactDetail
    success_url = '/'

