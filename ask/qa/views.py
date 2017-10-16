from django.shortcuts import render
from . import custom_pagination as pagination

# Create your views here.
from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return render(pagination(request, *args), 'templates'+kwargs['page_slug']+'.html')
