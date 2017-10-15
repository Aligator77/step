from django.apps import AppConfig


class QaConfig(AppConfig):
    name = 'qa'

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
    try:
        page = paginator.page(page)
    exept EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page
