# coding: utf-8
# ------------------------------------------
# 本views只使用简单的fun集合；
# 用类函数实现版本，放在views1中；
# ------------------------------------------
from django.shortcuts import render, HttpResponse
from .models import Dir, Magazine


# 功能：默认主页; 显示某一年的杂志目录；或空白页；
# url：""
# 参数: Magazine.object(***)
def index(request):
    return render(request, 'pjquery/index.html', {'magazines': Magazine.objects(year='2008', month='12')})


# 功能：在search bar上输入关键字，对杂志文章目录进行搜索；
# url：^search/
# 输入：inputwords：string；
# 输出：查询结果信息二维数组[[year, month, article_name, article_page],...]
def search_keywords(request):
    inputwords = str.strip(request.POST['inputwords'])
    if inputwords == "":
        return render(request, 'pjquery/index.html', {'magazines': []})
    else:
        # 先用MongoEngine，做一遍粗滤，然后再手动筛选出结果；受限于EmbededDocument；
        smallerSet = Magazine.objects(dir__article_name__icontains=inputwords)

        resultSet = []
        for i in smallerSet:
          for j in i.dir:
            if inputwords in j.article_name:
                resultSet.append([i.year, i.month, j.article_name, j.article_page])

        return render(request, 'pjquery/index.html', {'results': resultSet})


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
