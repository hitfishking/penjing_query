# coding: utf-8
# ------------------------------------------
# 本views只使用简单的fun集合；
# 用类函数实现版本，放在views1中；
# ------------------------------------------
from django.shortcuts import render, HttpResponse, redirect
from .models import Dir, Magazine
from django.http import JsonResponse

# 最早版本模板，没有任何样式，只显示原始数据。
# url：'^0/'
def index_0(request):
    return render(request, 'pjquery/index_0.html')  # 纯一次性显示，没有页内交互；


# 功能：boostrap标准table版主页;
# url：'^1/'
# 参数: Magazine.object(***)
def index_1(request):
    return render(request, 'pjquery/index_1.html', {'magazines': [] })


# 功能：boostrap-table插件版主页;
# url：'^2/'
def index_2(request):
    return render(request, 'pjquery/index_2.html')


# 功能：bootstrap标准table版search；在search bar上输入关键字，对杂志文章目录进行搜索；
# url：^1/search1/
# 输入：inputwords：string；
# 输出：查询结果信息二维数组[[year, month, article_name, article_page],...]
def search_1(request):
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

        return render(request, 'pjquery/index_1.html', {'results': resultSet})


# 功能：在search bar上输入关键字，对杂志文章目录进行搜索；
#      本action用于响应返回bootstrap-table的template(index_2.html)；
# url：^2/search2/
# 输入：inputwords：string；
# 输出：查询结果信息二维数组[[year, month, article_name, article_page],...]
#      以json格式返回;
def search_2(request):
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

