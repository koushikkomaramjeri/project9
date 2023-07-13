from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Reg
from .forms import RegForm,LoginForm
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class RegInput(View):
    def get(self,request):
        con_dic={"regform":RegForm()}
        return render(request,'input.html',context=con_dic)
class RegView(View):
    def post(self,request):
        rf=RegForm(request.POST)
        if rf.is_valid():
            r1=Reg(firstname=rf.cleaned_data['firstname'],
                   lastname=rf.cleaned_data["lastname"],
                   username=rf.cleaned_data["username"],
                   password=rf.cleaned_data["password"],
                   cpassword=rf.cleaned_data["cpassword"],
                   emailid=rf.cleaned_data["emailid"],
                   mobileno=rf.cleaned_data["mobileno"]
                   )
            r1.save()
            res=HttpResponse("reg success")
        return res
class LoginInput(View):
    def get(self,request):
        condic={"loginform":LoginForm()}
        return render(request,'logininput.html',context=condic)
class Login(View):
    def post(self,request):
        lf=LoginForm(request.POST)
        if lf.is_valid():
            objs=Reg.objects.filter(username=lf.cleaned_data["username"],password=lf.cleaned_data["password"])
            if objs:
                return HttpResponse("login success")
            else:
                return HttpResponse("login failed")