from django.db import models

# Create your models here.
class super_admin(models.Model):
    username=models.CharField(max_length=250,null=True)
    password=models.CharField(max_length=250,null=True)
    role=models.CharField(max_length=250,null=True)
    
    class Meta:
        db_table='super_admin'