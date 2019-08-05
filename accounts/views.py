from django.shortcuts import render , HttpResponseRedirect
from .models import Entries
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from excel_response import ExcelResponse

# Create your views here.


def home_redirect(request):
    return HttpResponseRedirect(reverse('home'))

def data_to_excel(request):
    data = Entries.objects.all()
    return ExcelResponse(data, output_filename='Accounts Data')


class EntryListView(ListView):
    model = Entries
    template_name = 'accounts/home.html'
    ordering = ['-id']


class EntryDetailView(DetailView):
    model = Entries



class EntryCreateView(CreateView):
    model = Entries
    fields = ['purchaser_name',
                'purchaser_address',
                'gstin_no',
                'description',
                'hsn_code',
                'quantity',
                'rate',
                'taxable_value',
                'packaging',
                'total_amount_before_tax',
                'cgst',
                'sgst',
                'total_amount_after_tax',]
    success_url = reverse_lazy('redirect')


class EntryUpdateView(UpdateView):
    model = Entries
    fields = ['purchaser_name',
              'purchaser_address',
              'gstin_no',
              'description',
              'hsn_code',
              'quantity',
              'rate',
              'taxable_value',
              'packaging',
              'total_amount_before_tax',
              'cgst',
              'sgst',
              'total_amount_after_tax',]
    success_url = reverse_lazy('redirect')


class EntryDeleteView(DeleteView):
    model = Entries
    success_url = reverse_lazy('redirect')
