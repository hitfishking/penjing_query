# coding: utf-8
# ------------------------------------------
# 本views只使用简单的fun集合；
# 用类函数实现版本，放在views1、views2中；
# ------------------------------------------
from django.shortcuts import render, HttpResponse, redirect
from .models import Dir, penjing
from django.http import JsonResponse
from django.core.paginator import Paginator

# import pydevd
# pydevd.settrace('192.168.0.4', port=21000, stdoutToServer=True, stderrToServer=True, suspend=False)


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
    print(request.POST['inputwords'])
    # inputwords = str.strip((request.POST['inputwords']).encode('utf-8')).encode('utf-8')
    inputwords = request.POST['inputwords']

    if inputwords == "":
        return redirect('index_1')
    else:
        # 先用MongoEngine，做一遍粗滤，然后再手动筛选出结果；受限于EmbededDocument；
        print("---------------------")
        smallerSet = penjing.objects(dir__article_name__icontains=inputwords)
        print(smallerSet)

        resultSet = []
        for i in smallerSet:
          for j in i.dir:
            if inputwords in j.article_name:
                resultSet.append([i.year, i.month, j.article_name, j.article_page])

        return render(request, 'pjquery/index_1.html', {'results': resultSet})   # post会导致整个页面更换；



# 功能：在search bar上输入关键字，对杂志文章目录进行搜索；
#      本action用于响应返回bootstrap-table的template(index_2.html)；
#      使用Django的Paginate分页功能；
#      使用Django的session存储状态数据的功能；
# url：^2/search2/
# 输入：inputwords：string；
# 输出：查询结果信息二维数组[[year, month, article_name, article_page],...]
#      以json格式返回;
# 要点：参考README.md
def search_2(request):
    # inputwords = str.strip((request.GET['inputwords']).encode('utf-8'))
    # inputwords = request.POST['inputwords']
    # inputwords = request.POST.get('inputwords')
    # inputwords = u'罗汉松'.encode('utf-8')
    inputwords = request.GET['inputwords']
    print(inputwords)

    pageIndex = request.GET['PageIndex']
    offSet = request.GET['offSet']
    pageSize =  request.GET['pageSize']

    def save_to_session(inputwords):
        smallerSet = penjing.objects(dir__article_name__icontains=inputwords)  # 粗滤

        articleSet = []
        counter = 0
        for i in smallerSet:  # 细滤
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
        paginator = Paginator(articleSet, pageSize)
        request.session['k_object_list'] = paginator.object_list  # 把paginator对象变成数组，用于session序列化；
        request.session['k_counter'] = counter

    if inputwords == "":
       return HttpResponse("No inputwords!")

    if str(pageIndex) == '1':   # 第1页 + 新运行(session无此key) + 新单词(与已有词不同的新词)；
       if ('inputwords' not in request.session) or (request.session['inputwords'] != inputwords):
          request.session['inputwords'] = inputwords
          save_to_session(inputwords)

    object_list = request.session['k_object_list']
    articles = Paginator(object_list, pageSize).page(pageIndex)  # 把session中存储的数组恢复成paginator对象，再取其中的page；
    counter = request.session['k_counter']
    data= {
        'total': counter,
        'rows': articles.object_list
    }

    return JsonResponse(data)


