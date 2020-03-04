from django.contrib import admin
from .models import CreditCardAsset,ActiveDirectoryAsset

# Register your models here.
admin.site.register(CreditCardAsset)
admin.site.register(ActiveDirectoryAsset)
