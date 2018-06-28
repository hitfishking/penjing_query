from django.shortcuts import render, HttpResponse
from .models import Dir, Magazine
from django.views.generic import View

# class Magazine_Controller(View):
#     def query_dir(self, request):
#         results = Magazine.objects.get(year='1985', month='1')
#         print(results[0].dir)
#         return HttpResponse('hello world')

def index(request):
    return render(request, 'pjquery/index.html')

def query_dir(request):
    results = Magazine.objects.get(year='1985', month='1')
    print(results[0].dir)
    return HttpResponse('hello world')

