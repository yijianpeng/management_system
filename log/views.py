from django.shortcuts import render, HttpResponse
from .models import Account


#主页面

#登录页面
def login(request):
    # 处理用户提交的表单数据
    return render(request, 'login.html')



# 登录按钮提交后，验证数据库中是否存在用户,存在就跳转主网页
def index(requst):
    u = requst.POST.get('username','')
    p = requst.POST.get('password','')
    if u and p:
        user = Account.objects.filter(name=u,password=p).count()
        if user>=1:
            return render(requst, 'index.html')
        else:
            error_msg='用户名或密码错误，请联系管理员'
            return render(requst, 'login.html',{'error_msg':error_msg})
    else:
        return render(requst, 'login.html')


#注册页面
def logon(request):
    # 渲染注册页面
    if request.method == 'POST':
        return render(request, 'login.html')
    
    return render(request, 'regist.html')

#退出页面
def logout(request):
    # 渲染退出页面
    return HttpResponse('退出')

