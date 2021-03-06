from django.shortcuts import render
from django.views import View
from staff.models import Staff
from assets.models import ActiveDirectoryAsset


class DashboardView(View):
    def get(self, request):
        return render(request, "dashboard.html",
                      {"staff_list": Staff.objects.all(), "assets_list": ActiveDirectoryAsset.objects.all()}, None,
                      None, None)
                      
class ITDashboardView(View):
    def get(self, request):
        return render(request, "it_dashboard.html",
                      {"staff_list": Staff.objects.all(), "assets_list": ActiveDirectoryAsset.objects.all()}, None,
                      None, None)
