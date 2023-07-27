from django.db import models

# Create your models here.
class Datas(models.Model):
    Name=models.CharField(max_length=20,default="")
    DOB=models.CharField(max_length=20,default="")
    Password=models.CharField(max_length=20,default="")
    Course=models.CharField(max_length=20,default="")
    Address=models.CharField(max_length=20,default="")
    Mail=models.CharField(max_length=20,default="")

    class Meta:
        managed=True
        db_table='first_app_datas'
    