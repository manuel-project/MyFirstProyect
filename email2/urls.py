from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miprmerproyeto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', "email2.views.email_consultar", name = "Email"),
)