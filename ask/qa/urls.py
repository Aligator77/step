'''/
/login/
/signup/
/ask/
/popular/
/new/
'''


#from django.conf.urls import url
#from qa.views import test
#from qa.views import test, question_list, question_detail, popular
#from qa.views import question_ask, question_answer
#from qa.views import user_signup, user_login, user_logout
'''
urlpatterns = [
    url(r'^$', question_list, name='question_list'),
    url(r'^question/(?P<pk>\d+)/', question_detail, name='question_detail'),
    url(r'^popular/', popular, name='popular'),
    url(r'^ask/', question_ask, name='question_ask'),
    url(r'^answer/', question_answer, name='question_answer'),
    url(r'^signup/', user_signup, name='signup'),
    url(r'^login/', user_login, name='login'),
    url(r'^logout/', user_logout, name='logout'),
    url(r'^new/', test, name='new'),
]
############
from django.conf.urls import url
from qa.views import test#, mainpg, question, popular, question_ask, question_ans, user_login, user_signup, user_logout

urlpatterns = [
	url(r'^$', mainpg, name='mainpg'),
	url(r'^question/(?P<pk>\d+)/$', question, name='question'),
	url(r'^popular/', popular, name='popular'),
	url(r'^ask/', question_ask, name='question_ask'),
	url(r'^answer/', question_ans, name='question_ans'),
	url(r'^new/', test, name='test'),
	url(r'^login/', user_login, name='login'),
	url(r'^signup/', user_signup, name='signup'),
	url(r'^logout/', user_logout, name='logout'),
]

'''
from django.conf.urls import url
from qa.views import test, main_page, question, popular#, ask, question_ans, login, reg, logout

urlpatterns =[
    url(r'^$',test,name='main_page', kwargs={'page_slug':'index'}),
    url(r'^(?P<page_slug>\w+)/$',test,name='all', kwargs={'page_slug':'page_slug'}),
    url(r'^(?P<page_slug>\w+)/(?P<id>\d+)/$',test,name='all_with_id',kwargs={'page_slug':'page_slug'}),
    url(r'^signup/$',test,name='reg'),
    url(r'^question/[!/d+!]/$',test,name='quest'),
    url(r'^ask/$',test,name='ask'),
    url(r'^popular/$',test,name='popular'),
    url(r'^new/',test,name='new'),
]
