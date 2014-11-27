from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'camilogonzalez.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'camilogonzalez.views.home', name='home'),
    url(r'^aboutMe/', 'camilogonzalez.views.aboutMe', name='aboutMe'),
    url(r'^contactMe/', 'camilogonzalez.views.contactMe', name='contactMe'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^blog/', include('blog.urls')),
)
