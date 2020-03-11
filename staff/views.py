from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Staff, Privilege
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from xhtml2pdf import pisa             # import python module
from io import BytesIO
from django.template.loader import get_template
import os
from django.conf import settings



class StaffProfile(DetailView):
    model = Staff
    template_name = "staff_profile.html"

    def get_context_data(self, **kwargs):
        context = super(StaffProfile, self).get_context_data(**kwargs)
        context['privileges'] = Privilege.objects.filter(staff=self.object)
        flags = [p.asset.get_flags() for p in Privilege.objects.filter(staff=self.object) if p.asset.get_flags()]
        all_hr=[u for u in User.objects.all() if u.groups.filter(name="HumanResource").exists() or u.groups.filter(name="IT").exists()]
        if self.request.user.groups.filter(name="HumanResource").exists():
            context["IS_HR"]=True
        else:
            context["IS_HR"]=False
        
        template = get_template('flag_log_report.html')
        html = template.render({"flags":flags})
        report_file_path=os.path.join(settings.MEDIA_ROOT,"reports/"+"flag_report.pdf")
        report_file = open(report_file_path, "w+b")
        pisaStatus = pisa.CreatePDF(html, dest=report_file)
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        report_file.close()
            
        attachments=[("ADAS_FLAG_REPORT.pdf",open(report_file_path,"rb").read(),'application/pdf')]
            
        email = EmailMessage(
            'Suspecious Activity Detected',
            'See attached the flagged suspecious activity',
            'terrymwangi05@gmail.com',
            [u.email for u in all_hr],
            [],
            reply_to=['terrymwangi05@gmail.com'],
            attachments=attachments
        )
        email.send()
        return context


class AddStaff(CreateView):
    model = Staff
    fields = ['first_name', 'last_name', 'id_number',
              'email', 'phone_number', 'employee_id', 'role']
    template_name = "add_staff.html"
    success_url = "/dashboard"


class UpdateStaff(UpdateView):
    model = Staff
    fields = ['first_name', 'last_name', 'description']
    template_name = "assets/update_asse.html"


class DeleteStaff(DeleteView):
    model = Staff
    template_name = "assets/delete_asset.html"
    success_url = reverse_lazy('asset-list')
