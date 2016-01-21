from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'async.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^celery_test/', 'sample.views.start_celery_task'),
    url(r'^celery_progress/(?p<task_id>\.*)/$', 'sample.views.monitor_celery_task'),


)
