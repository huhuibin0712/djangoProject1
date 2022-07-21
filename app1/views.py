from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'welcome.html', {"whichHTML": "home.html", "oid": "", "username": "胡会宾"})

@login_required
def welcome(request):
    # return HttpResponse('你好鸭！')
    return render(request, 'welcome.html')

def child(request,eid,oid):
    return render(request, eid)

def login(request):
    return render(request, 'login.html')

def login_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']
    from django.contrib import auth
    user = auth.authenticate(username=u_name,password=p_word)
    if user is not None:
        auth.login(request,user)
        request.session['user'] = u_name
        return HttpResponse('成功')
    else:
        return HttpResponse('失败')

def register_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']
    from django.contrib.auth.models import User
    try:
        user = User.objects.create_user(username=u_name,password=p_word)
        return HttpResponse('注册成功！')
    except:
        return HttpResponse('注册失败，用户名已经存在')

def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return HttpResponseRedirect('/login/')

def pei(request):
    tucao_test = request.GET['tucao_test']