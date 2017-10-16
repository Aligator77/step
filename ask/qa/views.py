from django.shortcuts import render
from . import custom_pagination as pagination

# Create your views here.
from django.http import HttpResponse 
def test(request, page_slug='index'):
    templ_type = page_slug;
    return render(request, templ_type+'.html')

def main_page(request):
    last_quesion = Question.objects.all().order_by('-id')
    return render(request, 'index.html', {'quest':last_question[:1]})

def question(request):
    return render(request, 'question.html')

def popular(request):
    quests = Question.objects.all().order_by('-likes')
    page = pagination(request,quest)
    return render(request, 'question.html', page)

