from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html");

def login_action(request):
    if request.method == 'POST':
        user = request.POST.get('user', '')
        pwd = request.POST.get('pwd','')
        if str(user).__len__() > 0:
            resp = HttpResponseRedirect('/event_manage/');
            #resp.set_cookie('uid',user,3600);
            #request.session['uid'] = user;
            credentials = {'username':user,'password':pwd};
            user = auth.authenticate(**credentials);
            if user != None:
                return resp;
    return render(request=request,template_name='index.html',context={"error":"params error"});

def event_manage(request):
    mSession = request.session.get('uid','');
    if mSession :
        return render(request, 'event_manage.html', {'uid': mSession});
    '''if request.COOKIES.get('uid') == 'admin':
        return render(request,'event_manage.html',{'uid':request.COOKIES.get('uid')});'''
    return HttpResponse('params error!!!');