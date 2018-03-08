from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import meta
from django.db.models import Q

@login_required(login_url='/accounts/login/')
def index(request):
    #return render(request, 'blog/index.html', context={'title':'my database','welcome':'metabolomics database'})
    meta_list = meta.objects.all().order_by('-updatetime')
    return render(request, 'blog/index.html', context = {'title':'my database','welcome':'metabolomics database', 'meta_list' : meta_list} )
    '''
    我们首先把 HTTP 请求传了进去，
    然后 render 根据第二个参数的值 blog/index.html 找到这个模板文件并读取模板中的内容。
    之后 render 根据我们传入的 context 参数的值把模板中的变量替换为我们传递的变量的值，
    {{ title }} 被替换成了 context 字典中 title 对应的值，
    同理 {{ welcome }} 也被替换成相应的值。
    '''


def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = "please input keyword"
        return render(request, 'blog/index.html', {'error_msg':error_msg})

    meta_list = meta.objects.filter(Q(metabolomics__icontains = q))
    if not meta_list:
        return render(request, 'blog/index.html',{'title':'my database','error_msg':'no result!','meta_list':meta_list})
    return render(request, 'blog/index.html',{'title':'my database','error_msg':error_msg,'meta_list':meta_list})

def sortindexmz(request):
    meta_list = meta.objects.all().order_by('mz')
    return render(request, 'blog/index.html', context = {'title':'my database','welcome':'metabolomics database', 'meta_list' : meta_list} )

def sortindexrt(request):
    meta_list = meta.objects.all().order_by('rt')
    return render(request, 'blog/index.html', context = {'title':'my database','welcome':'metabolomics database', 'meta_list' : meta_list} )
    
