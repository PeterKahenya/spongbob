from django.contrib import admin
from django.urls import path
from homepage.views import HomePage
from accounts.views import LoginView,SignupView
from dashboard.views import DashboardView,ITDashboardView
from staff.views import AddStaff,StaffProfile
from assets.views import AddCreditCard,AddActiveDirectoryAccount,AssignAsset,FlagsView
from assets.views import DisablePrivilege,EnablePrivilege
from accounts.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePage.as_view(),name="homepage"),
    path('audits',FlagsView.as_view(),name="audits"),
    path('staff/add', AddStaff.as_view(), name="add-staff"),
    path('staff/<pk>/', StaffProfile  .as_view(), name="staff-profile"),
    path('assets/credit-card/add', AddCreditCard.as_view(), name="add-credit-card"),
    path('asset/assign-asset', AssignAsset.as_view(), name="assign-asset"),
    path('disable', DisablePrivilege.as_view(), name="asset_disable"),
    path('enable', EnablePrivilege.as_view(), name="asset_enable"),
    path('assets/active-directory/add', AddActiveDirectoryAccount.as_view(), name="add-active-directory"),
    path('dashboard', DashboardView.as_view(), name="dashboard"),
    path('it', ITDashboardView.as_view(), name="it-dashboard"),
    path('login',LoginView.as_view(),name="login"),
    path('logout',logout_view,name="logout"),
    path('signup',SignupView.as_view(),name="signup")
]
