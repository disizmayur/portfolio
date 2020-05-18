from django.db import models

class job(models.Model):
    imagefun=models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)