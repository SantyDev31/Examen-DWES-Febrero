from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Disco
from .forms import DiscoForm

# Create your views here.
class crear_disco(CreateView):
    model = Disco
    form_class = DiscoForm   
    template_name = 'disco_form.html'
    success_url = '/disco_list/'

class discos_lista(ListView):
    model = Disco
    template_name = 'discos_list.html'
    context_object_name = 'Discos'


