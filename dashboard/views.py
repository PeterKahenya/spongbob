from django.shortcuts import render
from django.views import View
from staff.models import Staff
from assets.models import Asset

class DashboardView(View):
    def get(self,request):
        return render(request,"dashboard.html",{"staff_list":Staff.objects.all(),"assets_list":Asset.objects.all()},None,None,None)