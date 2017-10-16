from django.core.paginator import Paginator,EmptyPage
from django.http import Http404
import django.shortcuts

select_num = 10

def pagination(request,qs):
    try:
        page = int(request.GET.get('page',1))
    except ValueError:
        raise Http404
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if(limit > 100):
        limit = 10
    paginator = Paginator(qs,select_num)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page
