# coding: utf-8
# ------------------------------------------
# 在本局部pjquery app中定义urls.py；
# 尽量局部化，模块独立化，再全局引用，是django框架模块化思想的重要运用；
# ------------------------------------------
from django.conf.urls import url
from . import views
from . import views1

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^query/', views.query_dir, name='query_dir'),
]
