from django.db import models

# Create your models here.

class NewMoedel(models.Model):
    text = models.CharField(max_length=255, null=False)
    # CharField 문자열로 받을것  / 255개의 길이 / null false = 꼭 값이 input 되야한다