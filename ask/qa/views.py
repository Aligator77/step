from django.shortcuts import render
from . import custom_pagination as pagination

# Create your views here.
from django.http import HttpResponse 
def test(request, page_slug='index'):
    templ_type = page_slug;
    return render(request, templ_type+'.html')
