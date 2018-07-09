# coding: utf-8
# ------------------------------------------
# 在本局部pjquery app中定义urls.py；
# 尽量局部化，模块独立化，再全局引用，是django框架模块化思想的重要运用；
# ------------------------------------------
from django.conf.urls import url
from . import views, views2
from pjquery.views2 import Magazine_Controller

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^old/', views.index_old, name='index_old'),

    url(r'^query1/', Magazine_Controller.as_view(), name='query_dir1'),
    url(r'^query2/', views2.query_dir2, name='query_dir2'),

    url(r'^search/', views.search_keywords, name='search_keywords'),
    url(r'^search2/', views.search_keywords2, name='search_keywords2'),

]
