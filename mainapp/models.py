from django.db import models
from django.contrib.auth.models import User

class Suv(models.Model):
    brend=models.CharField(max_length=50)
    narx=models.PositiveIntegerField()
    litr=models.PositiveIntegerField()
    batafsil=models.TextField()

class Mijoz(models.Model):
    ism=models.CharField(max_length=50)
    tel=models.CharField(max_length=50)
    manzil=models.CharField(max_length=100)
    qarz=models.PositiveIntegerField(default=0)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

class Admin(models.Model):
    ism=models.CharField(max_length=50)
    yosh=models.PositiveIntegerField()
    ish_vaqti=models.CharField(max_length=50)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

class Haydovchi(models.Model):
    ism=models.CharField(max_length=50)
    tel=models.CharField(max_length=20)
    kiritilgan_sana=models.DateField(auto_now_add=True)

class Buyurtma(models.Model):
    suv=models.ForeignKey(Suv, on_delete=models.CASCADE)
    vaqt=models.DateField(auto_now_add=True)
    mijoz=models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor=models.CharField(max_length=50)
    narx=models.PositiveIntegerField()
    admin=models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi=models.ForeignKey(Haydovchi, on_delete=models.CASCADE)




