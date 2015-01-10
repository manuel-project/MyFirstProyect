from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miprmerproyeto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^clientes/', include("clientes.urls")), # clientes/ Es el nombre que quiero para la url.... clientes.urls Es el nombre de la app
    url('^email/', include("email2.urls")),
)