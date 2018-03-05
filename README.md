# django项目测试

根据 https://www.zmrenwu.com/post/ 来做网页

2/27 搞到 Django 博客首页视图[https://www.zmrenwu.com/post/7/]的一半

2/28
'''
In [1]: from blog.models import meta

In [2]: from django.utils import timezone

In [3]: from django.contrib.auth.models import User

In [5]: user =  User.objects.get(username = 'saber')

In [6]: c = meta(metabolomics = 'ccc', mz = 123.21, rt = 54215.26, user = user, updatetime = timezone.now())

In [7]: c.save()
'''

3/1
http://127.0.0.1:8000/admin 用户管理系统
接下来应该考虑的是用户登陆系统，权限管理
在首页加一个登陆的超链接链接到/admin就可以了。  

3/4
https://www.zmrenwu.com/post/44/ 查询系统应该怎么做？？？？
那个按钮加不上啊？

3/5

按钮加上了，可是又有了一个新的错误啦！