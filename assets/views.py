from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView,DeleteView
from .models import CreditCardAsset,Asset


class AddCreditCard(CreateView):
    model = CreditCardAsset
    fields = ['type_of_asset','name_of_asset','description','credit_card_number','credit_card_exp_date','credit_card_cvc','credit_card_issuer']
    template_name = "add_credit_card.html"

    success_url = "/dashboard"


class UpdateAsset(UpdateView):
    model = Asset
    fields = ['type_of_asset', 'name_of_asset', 'description']
    template_name = "assets/update_asset.html"

class DeleteAsset(DeleteView):
    model = Asset
    template_name = "assets/delete_asset.html"
    success_url = reverse_lazy('asset-list')





