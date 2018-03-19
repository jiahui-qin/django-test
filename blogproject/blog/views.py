from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  
from django.http import HttpResponse
from django.shortcuts import render
from .models import meta
from django.db.models import Q

@login_required(login_url='/accounts/login/')
def index(request):
    meta_list = meta.objects.all().order_by('-updatetime')
    #return HttpResponseRedirect(reverse(NAME_OF_PROFILE_VIEW, args=[request.user.username]))
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

def highsearch(request):
    lowmz = request.GET.get('lowmz')
    lowrt = request.GET.get('lowrt')
    highmz = request.GET.get('highmz')
    highrt = request.GET.get('highrt')
    if not lowmz:
        lowmz = 0
    if not highmz:
        highmz = float('inf')
    if not lowrt:
        lowrt = 0
    if not highrt:
        highrt = float('inf')
    error_msg = "no result!"
    meta_list = meta.objects.filter(Q(mz__gte = lowmz) & Q(mz__lte = highmz) & Q(rt__gte = lowrt) & Q(rt__lte = highrt))
    if not meta_list:
        return render(request, 'blog/index.html',{'title':'my database','error_msg':error_msg,'meta_list':meta_list})
    return render(request, 'blog/index.html',{'title':'my database','meta_list':meta_list})

def sortindexmz(request):
    meta_list = meta.objects.all().order_by('mz')
    return render(request, 'blog/index.html', context = {'title':'my database','welcome':'metabolomics database', 'meta_list' : meta_list} )

def sortindexrt(request):
    meta_list = meta.objects.all().order_by('rt')
    return render(request, 'blog/index.html', context = {'title':'my database','welcome':'metabolomics database', 'meta_list' : meta_list} )

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return HttpResponseRedirect('/index/')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render(request, 'blog/login.html', context = {'title':'my database','welcome':'metabolomics database', 'state':state} )

def logout_user(request):
  logout(request)
  # Redirect to a success page.
  return HttpResponseRedirect("/accounts/login/")
