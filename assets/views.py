from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from django.views.generic.edit import UpdateView,DeleteView
from .models import CreditCardAsset,ActiveDirectoryAsset,Asset
from staff.models import Privilege
import requests
import json


class AddCreditCard(CreateView):
    model = CreditCardAsset
    fields = ['type_of_asset','name_of_asset','description','credit_card_number','credit_card_exp_date','credit_card_cvc','credit_card_issuer']
    template_name = "add_credit_card.html"

    success_url = "/dashboard"

class AddActiveDirectoryAccount(CreateView):

    def get_token(self):
        url="https://login.microsoftonline.com/4370dcec-f44f-47ec-a5a6-2cd0ec017a72/oauth2/token"
        data={
            "grant_type":"client_credentials",
            "client_id":"bba23e01-d3e5-4ba3-b7bc-51ffada2ccf9",
            "client_secret":"v]h?-ih0f67A6h?Tp:x]H9qx.kLNH:XW",
            "resource":"https://graph.microsoft.com"
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        x=requests.post(url,data=data,headers=headers)

        return json.loads(x.text)["access_token"]

    def get(self,request):
        return render(request,"add_active_directory_account.html")

    def post(self,request):

        url = 'https://graph.microsoft.com/v1.0/users'
        auth_token=self.get_token()
        headers = {'Authorization': 'Bearer ' + auth_token}

        type_of_asset=request.POST.get("type_of_asset")
        name_of_asset=request.POST.get("name_of_asset")
        description=request.POST.get("description")
        username=request.POST.get("username")
        name=request.POST.get("name")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        groups=request.POST.get("groups")
        roles=request.POST.get("roles")
        block_sign_in=request.POST.get("block_sign_in")
        usage_location=request.POST.get("usage_location")
        job_title=request.POST.get("job_title")
        department=request.POST.get("department")
        password=request.POST.get("password")

        ad_user = ActiveDirectoryAsset()
        ad_user.type_of_asset=type_of_asset
        ad_user.name_of_asset=name_of_asset
        ad_user.description=description
        ad_user.username=username
        ad_user.name=name
        ad_user.first_name=first_name
        ad_user.last_name=last_name
        ad_user.groups=groups
        ad_user.roles=roles
        ad_user.block_sign_in=block_sign_in
        ad_user.usage_location=usage_location
        ad_user.job_title=job_title
        ad_user.department=department
        ad_user.save()


        ad_user_obj = {
                  "accountEnabled": True,
                  "displayName": first_name+last_name,
                  "mailNickname": username,
                  "userPrincipalName": name+"@terowamzgmail.onmicrosoft.com",
                  "passwordProfile" : {
                    "forceChangePasswordNextSignIn": True,
                    "password": password
                  }
                }

        response = requests.post(url, json=ad_user_obj, headers=headers)

        if response.status_code==201:
            return redirect("/dashboard")
        else:
            return render(request,"add_active_directory_account.html")

class AssignAsset(CreateView):
    model=Privilege
    fields=['asset','staff']
    template_name="assign_asset.html"

    success_url="/dashboard"


class DisablePrivilege(View):

    def post(self,request):
        p=Privilege.objects.filter(id=request.POST.get("p_id"))[0]
        p.asset.disable()
        p.status="DISABLED"
        p.save()
        
        return redirect()

class UpdateAsset(UpdateView):
    model = Asset
    fields = ['type_of_asset', 'name_of_asset', 'description']
    template_name = "assets/update_asset.html"

class DeleteAsset(DeleteView):
    model = Asset
    template_name = "assets/delete_asset.html"
    success_url = reverse_lazy('asset-list')





