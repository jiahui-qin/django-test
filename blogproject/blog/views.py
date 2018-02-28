from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import meta
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