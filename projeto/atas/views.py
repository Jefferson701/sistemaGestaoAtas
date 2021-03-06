from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin,  StaffRequiredMixin

from .models import Ata


class AtaListView(LoginRequiredMixin,  StaffRequiredMixin, ListView):
    model = Ata
    fields = ['codigo', 'data', 'hora', 'local', 'pauta', 'redator', 'texto', 'validada', 'integrantes']


class AtaCreateView(LoginRequiredMixin,  StaffRequiredMixin, CreateView):
    model = Ata
    fields = ['codigo', 'data', 'hora', 'local', 'pauta', 'redator', 'texto', 'validada', 'integrantes']
    success_url = 'ata_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Ata cadastrada com sucesso na plataforma!')
        return reverse(self.success_url)


class AtaUpdateView(LoginRequiredMixin,  StaffRequiredMixin, UpdateView):
    model = Ata
    fields = ['local', 'pauta', 'redator', 'texto', 'validada', 'integrantes']
    success_url = 'ata_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Dados da turma atualizados com sucesso na plataforma!')
        return reverse(self.success_url)


class AtaDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Ata
    success_url = 'ata_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à essa ata, permissão negada!')
        return redirect(self.success_url)