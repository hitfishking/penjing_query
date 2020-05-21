# coding: utf-8
# ------------------------------------------
# 本views1是用类函数实现的版本，
# 简单使用funcs的版本放在views1中；
# ------------------------------------------
from django.shortcuts import render, HttpResponse
from .models import Dir, penjing
from django.views.generic import View

# class Magazine_Controller(View):
#     def query_dir(self, request):
#         results = Magazine.objects.get(year='1985', month='1')
#         print(results[0].dir)
#         return HttpResponse('hello world')
