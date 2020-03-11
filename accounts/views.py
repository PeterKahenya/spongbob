from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("/")

class SignupView(View):
    def get(self, request):
        return render(request, "signup.html", {"ERRORS":""}, None, None, None)

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("email")
        #implement Phone Number
        password = request.POST.get("password")
        role = request.POST.get("role")


        user=User.objects.create_user(username=username,email=email,password=password)

        user.first_name = first_name
        user.last_name = last_name
        if role=="hr":
            user.groups.add(Group.objects.get(id=2))
        elif role=="it":
            user.groups.add(Group.objects.get(id=3))
        else:
            user.groups.add(Group.objects.get(id=1))
        
        user.save()

        if user is not None:
            return redirect("/", permanent=True)
        else:
            return render(request, "signup.html", {"ERRORS":"Something Went Wrong"}, None, None, None)


class LoginView(View):
    # def get(self,request):
    #     return render(request,"login.html",{"ERRORS":""},None,None,None)
    def post(self,request):
        username=request.POST.get("username")
        password=request.POST.get("password")
        print("Someone is loging in...")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)


            if user.groups.filter(name="HumanResource").exists():
                return redirect("/dashboard")
            elif user.groups.filter(name="IT").exists():
                return redirect("/it")
            elif user.groups.filter(name="Auditors").exists():
                return redirect("/audits")
            else:
                return redirect("/dashboard")
        else:
            return render(request,"index.html",{"ERRORS":"Invalid Credentials"},None,None,None)














