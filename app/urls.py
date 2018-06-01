from django.conf.urls import url
from . import views

# add url patterns for our views
# a url pattern is composed of a python regular expression
urlpatterns = [
    # post views
    url(r'^$', views.post_list, name='post_list'),
    
    # year requires 4 digits, month requires 2
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$,
        views.post_detail,
        name='post_detail'),
]