'''/
/login/
/signup/
/question/<123>/    # вместо <123> - произвольный ID
/ask/
/popular/
/new/
'''


from django.conf.urls import url
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
'''

urlpatterns =[
    url(r'^',url,name='all'),
    url(r'^login/$',url,name='login'),
    url(r'^signup/$',url,name='reg'),
    url(r'^auestion/[!/d+!]/$',url,name='quest'),
    url(r'^ask/$',url,name='ask'),
    url(r'^popular/$',url,name='popular'),
    url(r'^new/',url,name='new'),
]
