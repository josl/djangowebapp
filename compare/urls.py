from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /compare/
    url(r'^$', views.index, name='index'),
    # ex: /compare/user
    url(r'user', views.user, name='user'),
    # ex: /compare/group
    url(r'group', views.group, name='group')
]
