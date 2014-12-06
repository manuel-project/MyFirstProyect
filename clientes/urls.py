from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miprmerproyeto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^clientes$', "clientes.views.C_Registrar_View", name = "Clientes"),
)
