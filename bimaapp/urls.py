from django.conf.urls import url,include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.images ,name = 'welcome'),
    url(r'^image/(\d+)',views.welcome,name ='image'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^profile/$', views.display_profile, name='profile'), 
    url(r'^details/$', views.details, name='details'),
    url(r'^proposer/$', views.new_proposer, name='proposer'), 
    url(r'^lifeassured/$', views.new_lifeassured, name='lifeassured'), 
    url(r'^address/$', views.new_address, name='address'), 
    url(r'^occupation/$', views.new_occupation, name='occupation'), 
    url(r'^premiumpaymethod/$', views.new_premiumpaymethod, name='premiumpaymethod'), 
    url(r'^bankers_order/$', views.new_bankers_order, name='bankers_order'), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)