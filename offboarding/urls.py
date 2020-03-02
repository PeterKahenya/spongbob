from django.contrib import admin
from django.urls import path
from homepage.views import HomePage
from accounts.views import LoginView,SignupView
from dashboard.views import DashboardView
from staff.views import AddStaff,StaffProfile
from assets.views import AddCreditCard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePage.as_view(),name="homepage"),
    path('staff/add', AddStaff.as_view(), name="add-staff"),
    path('staff/<pk>', StaffProfile.as_view(), name="staff-profile"),

    path('assets/credit-card/add', AddCreditCard.as_view(), name="add-asset"),

    path('dashboard', DashboardView.as_view(), name="dashboard"),
    path('login',LoginView.as_view(),name="login"),
    path('signup',SignupView.as_view(),name="signup")
]
