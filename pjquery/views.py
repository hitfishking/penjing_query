# coding: utf-8
# ------------------------------------------
# 本views只使用简单的fun集合；
# 用类函数实现版本，放在views1中；
# ------------------------------------------
from django.shortcuts import render, HttpResponse, redirect
from .models import Dir, Magazine
from django.http import JsonResponse
import json

# 功能：默认主页; 显示某一年的杂志目录；或空白页；
# url：""
# 参数: Magazine.object(***)
def index(request):
    return render(request, 'pjquery/index2.html', {'magazines': [] })


# 功能：在search bar上输入关键字，对杂志文章目录进行搜索；
# url：^search/
# 输入：inputwords：string；
# 输出：查询结果信息二维数组[[year, month, article_name, article_page],...]
def search_keywords(request):
    inputwords = str.strip(request.POST['inputwords'])
    if inputwords == "":
        return redirect('index')
    else:
        # 先用MongoEngine，做一遍粗滤，然后再手动筛选出结果；受限于EmbededDocument；
        smallerSet = Magazine.objects(dir__article_name__icontains=inputwords)

        resultSet = []
        for i in smallerSet:
          for j in i.dir:
            if inputwords in j.article_name:
                resultSet.append([i.year, i.month, j.article_name, j.article_page])

        return render(request, 'pjquery/index.html', {'results': resultSet})


# 功能：在search bar上输入关键字，对杂志文章目录进行搜索；
#      本action用于响应返回bootstrap-table的template(index2.html)；
# url：^search2/
# 输入：inputwords：string；
# 输出：查询结果信息二维数组[[year, month, article_name, article_page],...]
#      以json格式返回;
def search_keywords2(request):
    inputwords = str.strip(request.GET['inputwords'])
    if inputwords == "":
        pass
    else:
        smallerSet = Magazine.objects(dir__article_name__icontains=inputwords)

        articleSet = []
        counter = 0
        for i in smallerSet:
          for j in i.dir:
            if inputwords in j.article_name:
                counter = counter + 1
                articleSet.append({
                    'id': counter,
                    'year': i.year,
                    'month': i.month,
                    'title': j.article_name,
                    'page': j.article_page
                })
        data= {
            'total': counter,
            'rows': articleSet
        }

        return JsonResponse(data)


def index_old(request):
    return render(request, 'pjquery/index_old.html')  # 每个应用app，模板都默认存储在该app的templates子目录下；
    # return HttpResponse("hello world！")


def query_dir(request):
    arr1=[]
    for i in Magazine.objects(year='2011',month='1'):
        for j in i.dir:
            arr1.append(j.article_name)
            arr1.append('<br/>')

    return HttpResponse(arr1)
