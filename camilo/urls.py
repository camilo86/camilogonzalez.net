from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'camilo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'camilo.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aboutMe/', 'camilo.views.aboutMe', name='aboutMe'),
    url(r'^cotactMe/', 'camilo.views.contactMe', name='contactMe'),
)
