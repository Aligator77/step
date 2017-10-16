from django.core.paginator import Paginator,EmptyPage
from django.http import Http404
import django.shortcuts

const select_num = 10

def pagination(request,qs):
    try:
        page = int(request.GET.get('page',1))
    exept ValueError:
        page = Http404
    try:
        limit = int(request.GET.get('limit', 10))
    exept ValueError:
        limit = 10
    if(limit > 100):
        limit = 10
    paginator = Paginator(qs,select_num)
    try:
        page = paginator.page(page)
    exept EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page
