from django.shortcuts import render,redirect
from . import forms

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.

def register(request):
    #! Bu birinci yontem fakat biraz daha zahmetli bir yontem bunun yerine
    """if request.method == "POST":
        form = forms.RegisterForm(request.POST) #* Formumuzu POST'tan gelen bilgilerle dolduruyoruz.

        if form.is_valid(): #* Ancak burada is_valid yaptigimizda django gidip clean fonksiyonunu calistiriyor.
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username=username)
            newUser.set_password(password)

            newUser.save() #* veritabanina kaydedildi.
            login(request=request,user=newUser)
            return redirect("index")
        context = {
            "form":form,
        }
        return render(request,"register.html",context)


    else:
        form = forms.RegisterForm()
        context = {
            "form":form,
        }
        return render(request,"register.html",context)"""
    
    form = forms.RegisterForm(request.POST or None) #* Burada Eger post request gelirse ona gore bir form olusturulcak eger GET request gelirse icine parametre almadan devam edecek

    if form.is_valid(): #* Ancak burada is_valid yaptigimizda django gidip clean fonksiyonunu calistiriyor.
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save() #* veritabanina kaydedildi.
        login(request=request,user=newUser)
        messages.success(request,"You are successfully Loged in.")
        return redirect("index")
    context = {
            "form":form,
        }
    return render(request,"register.html",context)


def loginUser(request):
    form = forms.LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Username or Password is not valid.")
            return render(request,"login.html",context)
        
        messages.success(request,"You are succesfully Loged in.")
        login(request,user)
        return redirect("index")
    return render(request=request,template_name="login.html",context=context)

def logoutUser(request):
    logout(request=request)
    messages.success(request,"You are successfully Logged out.")
    return redirect("index")
