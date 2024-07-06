from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View

# Create your views here.

def LandingView(request):
    return render(request,"landing.html")


def loginview(request):
    if request.method=='GET':
       return render(request,"login.html")
    elif request.method=='POST':
        uname=request.POST.get('un')
        pswd=request.POST.get('pw')
        # return HttpResponse(f"username :{uname} ,password :{pswd}")
        # return render(request,"login.html")
        return redirect('uhome')


class registerview(View):
    def get(self,request):
        return render(request,"register.html")
    def post(self,request):
        uname=request.POST.get('un')
        pswd=request.POST.get('pw')
        email=request.POST.get('em')
        return HttpResponse(f"username :{uname} ,password :{pswd}.email :{email}")
        
        



