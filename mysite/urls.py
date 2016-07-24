from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import hello,current_datetime,hours_ahead

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^admin/', include(admin.site.urls)),
     url('^hello/$',hello),
     url('^time/$',current_datetime),
     url('^time/plus/(\d{1,2})/$',hours_ahead),
     url('^admin/',include(admin.site.urls)),
)
