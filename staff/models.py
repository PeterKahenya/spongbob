from django.db import models
import uuid
from assets.models import Asset


class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    id_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    onboarded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name+" "+self.last_name
        
class Privilege(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    status = models.CharField(max_length=200,default="ENABLED")

    def __str__(self):
        return self.asset.name_of_asset+"   "+self.status
    
