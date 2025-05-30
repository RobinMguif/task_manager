from django.db import models

# Create your models here.
class super_admin(models.Model):
    username=models.CharField(max_length=250,null=True)
    password=models.CharField(max_length=250,null=True)
    role=models.CharField(max_length=250,null=True)
    
    class Meta:
        db_table='super_admin'
        
        
class user_admin(models.Model):
    username=models.CharField(max_length=150,null=True)
    password=models.CharField(max_length=150,null=True)
    name=models.CharField(max_length=150,null=True)
    email=models.CharField(max_length=150,null=True)
    phoneno=models.CharField(max_length=150,null=True)
    is_admin=models.IntegerField(null=True)
    delete_status=models.CharField(max_length=25,null=True)
    class Meta:
        db_table='user_admin'