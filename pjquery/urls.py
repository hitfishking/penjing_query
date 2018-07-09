# coding: utf-8
# ------------------------------------------
# 在本局部pjquery app中定义urls.py；
# 尽量局部化，模块独立化，再全局引用，是django框架模块化思想的重要运用；
# ------------------------------------------
from django.conf.urls import url
from . import views
from . import views2
from pjquery.views2 import Magazine_Controller

urlpatterns = [
    url(r'^0/$', views.index_0, name='index_0'),
    url(r'^1/$', views.index_1, name='index_1'),
    url(r'^2/$', views.index_2, name='index_2'),
    url(r'^$', views.index_2, name='index'),     # 默认显示bootstrap-table插件版主页；

    url(r'^1/search1/$', views.search_1, name='search_1'),
    url(r'^2/search2/$', views.search_2, name='search_2'),

    # ------------------------类controller版功能---------------
    url(r'^query1/', Magazine_Controller.as_view(), name='query_dir1'),
    url(r'^query2/', views2.query_dir, name='query_dir2'),
]
