# coding: utf-8
# ------------------------------------------
# 本views只使用简单的fun集合；
# 用类函数实现版本，放在views1中；
# ------------------------------------------
from django.shortcuts import render, HttpResponse
from .models import Dir, Magazine

def index(request):
    return render(request, 'pjquery/index.html')  # 每个应用app，模板都默认存储在该app的templates子目录下；
    # return HttpResponse("hello world！")

def query_dir(request):

    arr1=[]
    for i in Magazine.objects(year='2011',month='1'):
        for j in i.dir:
            arr1.append(j.article_name)
            arr1.append('<br/>')

    return HttpResponse(arr1)

