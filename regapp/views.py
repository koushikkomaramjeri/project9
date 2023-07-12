from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Reg
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class RegInput(View):
    def get(self,request):
        return render(request,'input.html')
class RegView(View):
    def post(self,request):
        fn=request.POST["t1"]
        ln=request.POST["t2"]
        un=request.POST["t3"]
        pwd=request.POST["t4"]
        cpwd=request.POST["t5"]
        email=request.POST["t6"]
        mob=int(request.POST["t7"])
        r1=Reg(firstname=fn,lastname=ln,username=un,password=pwd,cpassword=cpwd,emailid=email,mobileno=mob)
        r1.save()
        res=HttpResponse("reg success")
        return res
class LoginInput(View):
    def get(self,request):
        return render(request,'logininput.html')
class Login(View):
    def post(self,request):
        user=request.POST["un"]
        pwd=request.POST["pw"]
        objs=Reg.objects.filter(username=user,password=pwd)
        if objs:
            return HttpResponse("login success")
        else:
            return HttpResponse("login failed")