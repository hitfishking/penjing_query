# coding: utf-8
# ------------------------------------------
# 本views1是用类函数实现的版本，
# 简单使用funcs的版本放在views1中；
# ------------------------------------------
from django.shortcuts import render, HttpResponse
from .models import Dir, penjing
from django.views.generic import View

class Magazine_Controller(View):

    def get(self, request):
        arr1 = self.query_dir()

        return HttpResponse(arr1)

    def query_dir(self):
        arr1 = []
        arr1.append("Starting.... <br/>")
        for i in penjing.objects(year='2011', month='1'):
            for j in i.dir:
                arr1.append(j.article_name)
                arr1.append('<br/>')
        return arr1


# Class-based view 和 function-based view可以混合使用；
def query_dir(request):
    arr1=[]
    for i in penjing.objects(year='2011',month='1'):
        for j in i.dir:
            arr1.append(j.article_name)
            arr1.append('<br/>')

    return HttpResponse(arr1)

def show_sample(request):
    return render(request, 'pjquery/bootstrap-table-sample.html')

