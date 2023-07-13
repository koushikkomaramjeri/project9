from django import forms
class RegForm(forms.Form):
    firstname = forms.CharField(max_length=10)
    lastname = forms.CharField(max_length=10)
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10,widget=forms.PasswordInput())
    cpassword = forms.CharField(max_length=10,widget=forms.PasswordInput())
    emailid = forms.EmailField()
    mobileno = forms.IntegerField()
class LoginForm(forms.Form):
    username=forms.CharField(max_length=10)
    password=forms.CharField(max_length=10,widget=forms.PasswordInput())
